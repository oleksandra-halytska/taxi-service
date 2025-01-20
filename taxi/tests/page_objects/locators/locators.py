class Locators:
    LINK = "link"
    BUTTON = "button"

    USERNAME_LABEL = "Username:"
    PASSWORD_LABEL = "Password:"
    NAME_LABEL = "Name*"
    COUNTRY_LABEL = "Country*"
    SUBMIT = "Submit"

    UPDATE_BUTTON = "//*[contains(text(), 'Update')]"
    DELETE_BUTTON = "//*[contains(text(), 'Delete')]"

    USER_WITH_NAME_COUNTRY = \
        '//*[*[contains(text(), "{}")] and *[contains(text(), "{}")]]'
