
# sketchDB 🎨 
------------------------------

DESCRIPTION OF PROJECT:
sketchDB is a web-based application where users will be able to upload pdf versions of their sketches to store in the database. This creates an opportunity to use sketchDB as a single source of data management to keep all you and your colleague's sketch files in one place.
----------------------------------

LINKS:
GITHUB REPO: https://github.com/joewhitneywalker/sketchDB
HEROKU: https://jwsketchdb.herokuapp.com/

--------------------------------------
ABOUT:


THE PROBLEM:
THIS APPLICATION WAS CREATED TO SOLVE A PROBLEM. CURRENTLY MY TEAM HAS NO STANDARD FILE NAMING CONVENTIONS OR DATA ORGANIZATION STRUCTURE. THIS MAKES IT INCREDIBLY CHALLENGING TO SEARCH FOR TECHNICAL SKETCH FILES THAT YOU MAY NEED. THERE IS ALSO A LACK OF CENTRALIZATION, SO TO FIND EACH SKETCH YOU MUST DIG THROUGH WORKSPACES CREATED BY INDIVIDUALS. ADDITIONALLY, CROSS FUNCTIONAL TEAMS WHO NEED ACCESS TO THESE FILES NEED THEM IN DIFFERENT FORMATS. HOWEVER, UPLOADING THE DOCUMENT AS A PDF ALLOWS EACH TEAM TO OPEN THE FILE WITH THE SOFTWARE OF THEIR CHOOSING (ADOBE ILLUSTRATOR, ADOBE ACROBAT, READER, ETC). 

THE SOLVE:
I AM PROPOSING TO CREATE A WEB-BASED DATABASE THAT CAN HOLD ALL SKETCHES IN A .PDF FORMAT. EACH SKETCH MUST BE NAMED BY IT'S FIVE DIGIT STYLE NUMBER (ALSO KNOWN AS A PC5), TAGGED WITH THE CORRECT CATEGORY AND SEASON, AND HAVE CREATOR COMMENTS INSERTED FOR VERSION HISTORY. 

----------------------------------
TECHNOLOGIES USED:
✅ DJANGO
✅ PYTHON
✅ HTML5
✅ POSTGRES
✅ SQLITE
✅ CSS3
✅ GIT
✅ HEROKU
✅ BOOTSTRAP


---------------------------------

USER STORIES:
THE USER WILL BE ABLE TO UPLOAD AND MANAGE PDF FILES BY SORTING THROUGH SEASON OR CATEGORY. ADDITIONALLY, THE USER CAN CREATE A LIBRARY TO HOUSE SKETCHES THAT ARE USED OFTEN. THE USER WILL BE ABLE TO SEE THE VERSION HISTORY ON THE SKETCH DETAIL PAGE AND HAVE THE ABILITY TO DELETE & EDIT THEIR FILE NAMES AND COMMENTS, DELETE OTHER'S FILES, AND VIEW-ONLY OTHER'S COMMENTS. THE USER WILL ALSO HAVE THE ABILITY TO CANCEL THEIR DELETE REQUEST VIA A POP UP WINDOW THAT ASKS THEM IF THEY REALLY WANT TO DELETE. 

THE USER WILL BE ABLE TO UPDATE THEIR PASSWORD IN THEIR ACCOUNT, BUT THEIR NAME AND LOG INS WOULD BE STATIC, SET BY THE COMPANY. THE USER WILL BE ABLE TO SIGN OUT FROM THE DROP DOWN ARROW BY THEIR NAME, AND NAVGIATE TO HOME BY CLICKING ON THE "HOME" MENU NAV OR THE "LEVIS" ICON. ADDITIONALLY THE USER WILL BE ABLE TO NAVIGATE THROUGH SELECTING A MENU ITEM ON THE NAV BAR. 

------------------------------------

FUTURE ENHANCEMENTS:
CURRENTLY, THERE IS A SEARCH ICON IN THE HEADER THAT REDIRECTS THE USER TO THE FILE SEARCH VIEW. IN THE FUTURE, I WILL UPDATE THIS APPLICATION WITH THE ABILITY TO SEARCH FOR A FILE FROM ANY PAGE, RATHER THAN BEING REDIRECTED. 

------------------------------------

HOW TO USE:
-CREATE AN ACCOUNT & LOG IN
-NAVIGATE TO ALL FILES & SELECT UPLOAD FILE OR NAVIGATE TO UPLOAD FILE ON THE LEFT HAND NAV BAR
-FILL OUT THE REQUIRED FIELDS AND UPLOAD YOUR FILE
-TO SEARCH FOR A SPECIFIC STYLE, SELECT SEARCH FROM LEFT HAND NAV BAR AND ENTER SEARCH INTO THE SEARCH FIELD
-TO SEARCH BY SEASON OR CATEGORY, SELECT THE DROP DOWN MENUS TO THE LEFT OF THE SEARCH FIELD
-TO LEARN MORE ABOUT A SKETCH, DOWNLOAD, UPDATE OR DELETE, CLICK ON THE SKETCH NAME, AND SELECT THE ACTION YOU WOULD LIKE TO DO.
-USE THIS AS A WAY TO KEEP YOUR FILES ORGANIZED, STORED AND IN ONE PLACE FOR MULTIPLE USERS TO ACCESS


-------------------------------------

BRAIN STORM / USER STORIES:
![PROJECT 2 - BRAINSTORM_USER STORIES ](https://user-images.githubusercontent.com/92687151/160759285-2f7c456e-687b-4202-86d2-0f64add8ff35.jpg)


-------------------------------------
PROJECT WIREFRAME:
[PROJECT 4 WIREFRAME.pdf](https://github.com/joewhitneywalker/sketchDB/files/8385941/PROJECT.4.WIREFRAME.pdf)


-------------------------------------
DATA MODELS:
DATA MODEL 1:
1:M: THERE WILL BE ONCE STYLE NUMBER (PC5) THAT WILL RENDER MANY VERSIONS OF IT (FROM PREVIOUS SEASON)

DATA MODEL 2: 
M:M: AS THE SKETCHES ARE ALSO SEARCHABLE BY SEASON, CATEGORY OR BOTH, THERE ARE MANY SKETCHES TO MANY SEASONS. 

USER MODEL:
1:M: AS THE USER (1) CAN CREATE SEVERAL SKETCHES (MANY) AND SEVERAL COMMENTS (MANY)

ERD
![Project 4](https://user-images.githubusercontent.com/92687151/160977178-7c6cc230-a1c0-4506-b499-bd5d3d247d93.png)


------------------------------------
CODE SNIPPET:
MY FAVORIETE PIECE OF CODE IS THIS FILE LIST FUNCTION WHICH RENDERS OUT ALL THE FILES, LETS THE USER SEARCH FOR A FILE OR FILTER BY SEASON OR CATEGORY. I SPENT THE BULK OF MY TIME WORKING THROUGH THIS FUNCTION. 
![Screen Shot 2022-04-11 at 5 50 20 PM](https://user-images.githubusercontent.com/92687151/162856640-4a044c8a-57b1-4dfe-aba8-4c53d397859b.png)
-------------------------------------
PREVIEW:

-------------------------------------
THANK YOU FOR READING MY README :)
