*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    Chrome
${URL}    https://shopee.co.th/?gad_source=1&gclid=Cj0KCQiAwOe8BhCCARIsAGKeD57fckFGAe4jnwnokSWr8nI31Xyh5lm7yh9S1EziDpfq_K0ixEF6HPEaAmTHEALw_wcB
${SEARCH_TEXT}    baby toys

*** Test Cases ***
Enter Shopee website, landing on home page with EN lang
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    10
    ##Click Button    class="shopee-popup__close-btn"
    Mouse Over    class="stardust-popover"
    #Click Element    class="stardust-popover"
    #Capture Page Screenshot
    [Teardown]    Close Browser

Search for keywords “ baby toys “
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text    class="shopee-searchbar shopee-searchbar--focus"    baby toys
    Press Key    class="shopee-searchbar shopee-searchbar--focus"    ENTER
    Sleep    10
    [Teardown]    Close Browser