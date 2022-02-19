import json

class Person:
    def __init__(self, name, owes={}, owed_by={}, balance=0.0) -> None:
        self.name = name
        self.owes = owes
        self.owed_by = owed_by
        self.balance = balance

class RestAPI:
    def __init__(self, database=None):
        self.people = {}
        for person in database["users"]:
            self.people.update({person["name"]: Person(person["name"], 
                                                        person["owes"], 
                                                        person["owed_by"], 
                                                        person["balance"])})

    def get(self, url, payload=None):
        if not self.people:
            return '{"users": []}'
        else:
            p_name = json.loads(payload)["users"][0]
            return json.dumps({"users":[{"name": self.people[p_name].name, 
                                        "owes": self.people[p_name].owes, 
                                        "owed_by": self.people[p_name].owed_by, 
                                        "balance": self.people[p_name].balance}]})


    def post(self, url, payload=None):
        if url == "/add":
            person_name = json.loads(payload)["user"]
            self.people.update({person_name:Person(person_name)})

            return json.dumps({"name": self.people[person_name].name,
                                "owes": {},
                                "owed_by": {},
                                "balance": 0.0 })

        elif url == "/iou":
            iou = json.loads(payload)

            if iou["lender"] in self.people[iou["borrower"]].owed_by:
                if self.people[iou["borrower"]].owed_by[iou["lender"]] < iou["amount"]:
                    self.people[iou["borrower"]].owes.update({iou["lender"]: iou["amount"] - self.people[iou["borrower"]].owed_by[iou["lender"]]})
                    self.people[iou["borrower"]].owed_by.pop(iou["lender"])
                    self.people[iou["lender"]].owed_by.update({iou["borrower"]: iou["amount"] - self.people[iou["lender"]].owes[iou["borrower"]]})
                    self.people[iou["lender"]].owes.pop(iou["borrower"])


                elif self.people[iou["borrower"]].owed_by[iou["lender"]] > iou["amount"]:
                    self.people[iou["borrower"]].owed_by[iou["lender"]] -= iou["amount"]
                    self.people[iou["lender"]].owes[iou["borrower"]] -= iou["amount"]
                else:
                    self.people[iou["lender"]].owes.pop(iou["borrower"])
                    self.people[iou["borrower"]].owed_by.pop(iou["lender"])
            else:
                self.people[iou["lender"]].owed_by.update({iou["borrower"]: iou["amount"]})
                self.people[iou["borrower"]].owes.update({iou["lender"]: iou["amount"]})

            self.people[iou["lender"]].balance += iou["amount"]
            self.people[iou["borrower"]].balance -= iou["amount"]
            
            sorted_res = sorted([("borrower", iou["borrower"]), ("lender", iou["lender"])], key=lambda x: x[1])

            return json.dumps({"users": [{"name": self.people[iou[sorted_res[0][0]]].name,
                                            "owes": self.people[iou[sorted_res[0][0]]].owes,
                                            "owed_by": self.people[iou[sorted_res[0][0]]].owed_by,
                                            "balance": self.people[iou[sorted_res[0][0]]].balance},
                                            {"name": self.people[iou[sorted_res[1][0]]].name,
                                            "owes": self.people[iou[sorted_res[1][0]]].owes,
                                            "owed_by": self.people[iou[sorted_res[1][0]]].owed_by,
                                            "balance": self.people[iou[sorted_res[1][0]]].balance}]})

