def is_aria_checked(element, expected_value):
    aria_checked = element.get_attribute('aria-checked')
    return aria_checked == expected_value
