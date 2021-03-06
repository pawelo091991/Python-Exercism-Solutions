def handle_error_by_throwing_exception():
    raise Exception("Exception raise")


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        return True, int(input_data)
    except:
        return False, None


def filelike_objects_are_closed_on_exception(filelike_object):
    filelike_object.open()
    try:
        filelike_object.do_something()
        filelike_object.close()
    except:
        filelike_object.close()
        raise Exception("Error by function do_something()")
