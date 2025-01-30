*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    Chrome
${URL}    https://shopee.co.th/?gad_source=1&gclid=Cj0KCQiAwOe8BhCCARIsAGKeD57fckFGAe4jnwnokSWr8nI31Xyh5lm7yh9S1EziDpfq_K0ixEF6HPEaAmTHEALw_wcB
${SEARCH_TEXT}    baby toys
${SEARCH_BOX}    class="shopee-searchbar shopee-searchbar--focus"

*** Test Cases ***
Enter Shopee website, landing on home page with EN lang
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    10
    ##Click Button    class="fNzlSz"
    Mouse Over    class="stardust-popover"
    #Click Element    class="stardust-popover"
    #Capture Page Screenshot
    [Teardown]    Close Browser

Search for keywords “ baby toys “
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text    ${SEARCH_BOX}    baby toys
    Press Key    ${SEARCH_BOX}    ENTER
    Sleep    10
    [Teardown]    Close Browser

Website display search result as a list
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Element Is Visible    ${SEARCH_BOX}
    Input Text    class="shopee-searchbar shopee-searchbar--focus"    baby toys
    Click Button    ${SEARCH_BOX}
    ${results_count} =    Get Element Count    ${RESULT_LIST}//*  
    Should Be True    ${results_count} > 0    Search results should be displayed as a list
    Capture Page Screenshot
    [Teardown]    Close Browser