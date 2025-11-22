class Locators:
    LINK = "link"
    BUTTON = "button"

    USERNAME_LABEL = "Username"
    PASSWORD_LABEL = "Password"
    NAME_LABEL = "Name*"
    LICENSE_LABEL = "License number*"
    MODEL_LABEL = "Model*"
    COUNTRY_LABEL = "Country*"
    SUBMIT = "Submit"
    UPDATE = "Update"

    UPDATE_BUTTON = "//*[contains(text(), 'Update')]"
    DELETE_BUTTON = "//*[contains(text(), 'Delete')]"
    USER_WITH_PROPERTIES = \
        '//*[*[contains(text(), "{}")] and *[contains(text(), "{}")]]'
