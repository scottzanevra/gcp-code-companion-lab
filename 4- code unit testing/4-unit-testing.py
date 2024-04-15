

# ************************** Code Companion Prompt ***********************************
# highlight the function below and select generate unit tests


def extract_email(string):
    pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    return  pattern



def inner_join(list1, list2):
    result = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                result.append(item1)
    return result
