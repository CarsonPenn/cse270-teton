{
  "id": "616cab29-6d2a-477e-873a-3e8416073b73",
  "version": "2.0",
  "name": "smoke.side",
  "url": "https://carsonpenn.github.io/cse270-teton/admin.html",
  "tests": [{
    "id": "99fafa9f-bfb5-4ed3-9b5e-3d29239917b7",
    "name": "homepage",
    "commands": [{
      "id": "2dbca18f-3940-47aa-b7a8-ba1d1672da36",
      "comment": "",
      "command": "open",
      "target": "https://carsonpenn.github.io/cse270-teton/join.html",
      "targets": [],
      "value": ""
    }, {
      "id": "fb437d40-db91-440d-baf9-a317402b7f1a",
      "comment": "",
      "command": "setWindowSize",
      "target": "1154x1048",
      "targets": [],
      "value": ""
    }, {
      "id": "a801cb0e-cefe-419d-b4d8-0e7b92f13d82",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.header-logo img",
      "targets": [
        ["css=.header-logo img", "css:finder"],
        ["xpath=//img[@alt='Teton Chamber of Commerce Logo']", "xpath:img"],
        ["xpath=//div[@id='content']/header/div/div/a/img", "xpath:idRelative"],
        ["xpath=//img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "db1ea575-e27c-4bc3-a0aa-8f5fdb19b04b",
      "comment": "",
      "command": "verifyText",
      "target": "css=h1",
      "targets": [
        ["css=h1", "css:finder"],
        ["xpath=//div[@id='content']/header/div/div[2]/h1", "xpath:idRelative"],
        ["xpath=//h1", "xpath:position"],
        ["xpath=//h1[contains(.,'Teton Idaho')]", "xpath:innerText"]
      ],
      "value": "Teton Idaho"
    }, {
      "id": "e693f6ec-aae2-4ee9-b81c-5e7516cbb82a",
      "comment": "",
      "command": "verifyText",
      "target": "css=h2",
      "targets": [
        ["css=h2", "css:finder"],
        ["xpath=//div[@id='content']/header/div/div[2]/h2", "xpath:idRelative"],
        ["xpath=//h2", "xpath:position"],
        ["xpath=//h2[contains(.,'Chamber of Commerce')]", "xpath:innerText"]
      ],
      "value": "Chamber of Commerce"
    }, {
      "id": "7754dd52-e8b6-4da8-a13e-e15d6c2e2c9a",
      "comment": "",
      "command": "verifyTitle",
      "target": "Teton Idaho CoC",
      "targets": [],
      "value": ""
    }]
  }, {
    "id": "95338201-faaf-450f-be1a-26da9dc160aa",
    "name": "spotlight/joinlink",
    "commands": [{
      "id": "d34fce07-ad5f-4f8c-b8e2-3696b146874f",
      "comment": "",
      "command": "open",
      "target": "https://carsonpenn.github.io/cse270-teton/index.html",
      "targets": [],
      "value": ""
    }, {
      "id": "f7fd8af4-ac73-421b-b382-d17c5014d9dc",
      "comment": "",
      "command": "setWindowSize",
      "target": "1154x1048",
      "targets": [],
      "value": ""
    }, {
      "id": "63a45080-b8af-4b52-9dea-da064de9ff93",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight1 > h4",
      "targets": [
        ["css=.spotlight1 > h4", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div/h4", "xpath:idRelative"],
        ["xpath=//h4", "xpath:position"],
        ["xpath=//h4[contains(.,'Teton Elementary')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "2bc190b3-10be-44dd-acd4-765c6ee3a3e1",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight1 img",
      "targets": [
        ["css=.spotlight1 img", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div/p/a/img", "xpath:idRelative"],
        ["xpath=//p/a/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b211ec71-551d-4078-bd81-f31eb4454e93",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight1 > p:nth-child(3)",
      "targets": [
        ["css=.spotlight1 > p:nth-child(3)", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div/p[2]", "xpath:idRelative"],
        ["xpath=//div/p[2]", "xpath:position"],
        ["xpath=//p[contains(.,'126 Main Street, Teton, ID 83451')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "b2acc39c-4d9c-46ea-9634-4664a1ae0a91",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight1 > p:nth-child(4)",
      "targets": [
        ["css=.spotlight1 > p:nth-child(4)", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div/p[3]", "xpath:idRelative"],
        ["xpath=//div/p[3]", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Elementary has been around a long, long time.')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "e2695a23-34a8-4dc4-9add-2908134168d4",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight2 > h4",
      "targets": [
        ["css=.spotlight2 > h4", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div[2]/h4", "xpath:idRelative"],
        ["xpath=//div[2]/h4", "xpath:position"],
        ["xpath=//h4[contains(.,'Teton Post Office')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "48d3d067-7404-4ea0-bf3b-5df6058b4535",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight2 img",
      "targets": [
        ["css=.spotlight2 img", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div[2]/p/a/img", "xpath:idRelative"],
        ["xpath=//div[2]/p/a/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "c2ecc9a3-2dd3-4e0b-8f7d-b03053394f6c",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight2 > p:nth-child(3)",
      "targets": [
        ["css=.spotlight2 > p:nth-child(3)", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div[2]/p[2]", "xpath:idRelative"],
        ["xpath=//div[2]/p[2]", "xpath:position"],
        ["xpath=//p[contains(.,'8 East Main Street, Teton, ID 83451')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "33022d62-dc25-4e87-b660-f2decd66a8af",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.spotlight2 > p:nth-child(4)",
      "targets": [
        ["css=.spotlight2 > p:nth-child(4)", "css:finder"],
        ["xpath=//div[@id='content']/main/section[5]/div[2]/p[3]", "xpath:idRelative"],
        ["xpath=//div[2]/p[3]", "xpath:position"],
        ["xpath=//p[contains(.,'All your postal needs in one small place.')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "ad8b407e-b6a7-419b-96d8-53d0905520fa",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "linkText=Join Us!",
      "targets": [
        ["linkText=Join Us!", "linkText"],
        ["css=.a-button:nth-child(1)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us!')]", "xpath:link"],
        ["xpath=//div[@id='content']/main/section[6]/p[2]/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[3]", "xpath:href"],
        ["xpath=//p[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us!')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "d66ecd6d-0b5b-4f20-b831-b0d6c7303597",
      "comment": "",
      "command": "click",
      "target": "linkText=Join Us!",
      "targets": [
        ["linkText=Join Us!", "linkText"],
        ["css=.a-button:nth-child(1)", "css:finder"],
        ["xpath=//a[contains(text(),'Join Us!')]", "xpath:link"],
        ["xpath=//div[@id='content']/main/section[6]/p[2]/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'join.html')])[3]", "xpath:href"],
        ["xpath=//p[2]/a", "xpath:position"],
        ["xpath=//a[contains(.,'Join Us!')]", "xpath:innerText"]
      ],
      "value": ""
    }]
  }, {
    "id": "0ffc610e-9f76-42de-8559-fc980f11b8f4",
    "name": "directory",
    "commands": [{
      "id": "f71bc2c2-18e2-49eb-b306-883fce72e1c4",
      "comment": "",
      "command": "open",
      "target": "https://carsonpenn.github.io/cse270-teton/directory.html",
      "targets": [],
      "value": ""
    }, {
      "id": "bc5f67d1-b766-402f-8f7f-5b631fc4d63a",
      "comment": "",
      "command": "setWindowSize",
      "target": "1154x1048",
      "targets": [],
      "value": ""
    }, {
      "id": "4d1410bd-701a-420b-9d3c-c46efd8c5962",
      "comment": "",
      "command": "click",
      "target": "id=directory-grid",
      "targets": [
        ["id=directory-grid", "id"],
        ["css=#directory-grid", "css:finder"],
        ["xpath=//button[@id='directory-grid']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button", "xpath:idRelative"],
        ["xpath=//div/button", "xpath:position"],
        ["xpath=//button[contains(.,'GRID')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "a89d0ac1-7b45-45f6-af8a-4c08d3ba7f9d",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.gold-member:nth-child(9) > img",
      "targets": [
        ["css=.gold-member:nth-child(9) > img", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/img", "xpath:idRelative"],
        ["xpath=//section[9]/img", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "209bfc0e-2970-4d0b-8bd8-c1e21ce51be6",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "0d14a000-9328-466b-8aed-7b11af5a38c1",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(3)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(3)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p[2]", "xpath:idRelative"],
        ["xpath=//section[9]/p[2]", "xpath:position"],
        ["xpath=//p[contains(.,'4735 East Hwy 33')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "97d46558-1487-42e2-8549-adf328422f09",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(4)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(4)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p[3]", "xpath:idRelative"],
        ["xpath=//section[9]/p[3]", "xpath:position"],
        ["xpath=//p[contains(.,'Sugar City, ID 83448')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "46e6f558-713e-4a50-9929-4b8d7a09b1ae",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.gold-member:nth-child(9) a",
      "targets": [
        ["css=.gold-member:nth-child(9) a", "css:finder"],
        ["xpath=(//a[contains(text(),'Website')])[9]", "xpath:link"],
        ["xpath=//div[@id='directory-data']/section[9]/p[4]/a", "xpath:idRelative"],
        ["xpath=//a[@href='http://www.tetonturf.com/']", "xpath:href"],
        ["xpath=//section[9]/p[4]/a", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "c9a2c769-a4cc-457e-8451-e572747ef23b",
      "comment": "",
      "command": "verifyText",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": "Teton Turf and Tree"
    }, {
      "id": "ba7887e9-a8dc-4eec-90d4-45fde6907ded",
      "comment": "",
      "command": "click",
      "target": "id=directory-list",
      "targets": [
        ["id=directory-list", "id"],
        ["css=#directory-list", "css:finder"],
        ["xpath=//button[@id='directory-list']", "xpath:attributes"],
        ["xpath=//div[@id='directory-selector']/button[2]", "xpath:idRelative"],
        ["xpath=//button[2]", "xpath:position"],
        ["xpath=//button[contains(.,'LIST')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "26937755-97fd-4108-9cfd-7cb4082ca9f2",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "dfee50b2-221e-4ecf-810e-6e8d46ec52ae",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(3)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(3)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p[2]", "xpath:idRelative"],
        ["xpath=//section[9]/p[2]", "xpath:position"],
        ["xpath=//p[contains(.,'4735 East Hwy 33')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "084d0d4f-4146-4c28-ac31-2b47c7347734",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(4)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(4)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p[3]", "xpath:idRelative"],
        ["xpath=//section[9]/p[3]", "xpath:position"],
        ["xpath=//p[contains(.,'Sugar City, ID 83448')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "6133a744-10f4-45e7-a8fa-b86c67a08d7e",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "css=.gold-member:nth-child(9) a",
      "targets": [
        ["css=.gold-member:nth-child(9) a", "css:finder"],
        ["xpath=(//a[contains(text(),'Website')])[9]", "xpath:link"],
        ["xpath=//div[@id='directory-data']/section[9]/p[4]/a", "xpath:idRelative"],
        ["xpath=//a[@href='http://www.tetonturf.com/']", "xpath:href"],
        ["xpath=//section[9]/p[4]/a", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7061974d-5b96-4afa-a449-d7f1ee896f64",
      "comment": "",
      "command": "verifyText",
      "target": "css=.gold-member:nth-child(9) > p:nth-child(2)",
      "targets": [
        ["css=.gold-member:nth-child(9) > p:nth-child(2)", "css:finder"],
        ["xpath=//div[@id='directory-data']/section[9]/p", "xpath:idRelative"],
        ["xpath=//section[9]/p", "xpath:position"],
        ["xpath=//p[contains(.,'Teton Turf and Tree')]", "xpath:innerText"]
      ],
      "value": "Teton Turf and Tree"
    }]
  }, {
    "id": "79b7473f-cbe1-4eda-843a-2abab2886839",
    "name": "join",
    "commands": [{
      "id": "375d071c-00d2-4a8b-bea1-6be9d3dca4ef",
      "comment": "",
      "command": "open",
      "target": "https://carsonpenn.github.io/cse270-teton/join.html",
      "targets": [],
      "value": ""
    }, {
      "id": "5dc2c194-2f01-4854-b46f-ba7997fbdd11",
      "comment": "",
      "command": "setWindowSize",
      "target": "1154x1048",
      "targets": [],
      "value": ""
    }, {
      "id": "9f4fd0ae-5583-4c0e-896a-a2bf10adc2d8",
      "comment": "",
      "command": "click",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "b6e4ea36-099d-4fd1-a90c-8c349ba0601e",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "df8b81c8-2693-4b9b-b1dc-0b94bea38bce",
      "comment": "",
      "command": "type",
      "target": "name=fname",
      "targets": [
        ["name=fname", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='fname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "Coleman"
    }, {
      "id": "5fc887cf-1715-45fe-94e5-8a6ef1f8db53",
      "comment": "",
      "command": "click",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "6c0c261c-5f28-43b9-8cd6-4357b720629f",
      "comment": "",
      "command": "type",
      "target": "name=lname",
      "targets": [
        ["name=lname", "name"],
        ["css=.myinput:nth-child(3) > input", "css:finder"],
        ["xpath=//input[@name='lname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "Trebor"
    }, {
      "id": "36a78deb-6e30-47a3-9776-ef489f0ee1a7",
      "comment": "",
      "command": "click",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "ef6599b1-47dc-4158-ae33-25b5e96d2583",
      "comment": "",
      "command": "type",
      "target": "name=bizname",
      "targets": [
        ["name=bizname", "name"],
        ["css=.myinput:nth-child(4) > input", "css:finder"],
        ["xpath=//input[@name='bizname']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[3]/input", "xpath:idRelative"],
        ["xpath=//label[3]/input", "xpath:position"]
      ],
      "value": "Jedi Order"
    }, {
      "id": "e8ea61da-1692-4c82-bb4a-5796552716e8",
      "comment": "",
      "command": "click",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "bf5a46b8-7ba0-40ca-b6f7-1d6a218326f8",
      "comment": "",
      "command": "type",
      "target": "name=biztitle",
      "targets": [
        ["name=biztitle", "name"],
        ["css=.myinput:nth-child(5) > input", "css:finder"],
        ["xpath=//input[@name='biztitle']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[4]/input", "xpath:idRelative"],
        ["xpath=//label[4]/input", "xpath:position"]
      ],
      "value": "Jedi Master"
    }, {
      "id": "e51b8f54-c40c-45d2-a174-eea978bb6ad9",
      "comment": "",
      "command": "click",
      "target": "name=submit",
      "targets": [
        ["name=submit", "name"],
        ["css=input:nth-child(6)", "css:finder"],
        ["xpath=//input[@name='submit']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "13afd086-a721-4f3a-9ce9-baa21e87f358",
      "comment": "",
      "command": "click",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "64632d39-d72f-4d57-86fc-4009e460804f",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "name=email",
      "targets": [
        ["name=email", "name"],
        ["css=.myinput:nth-child(2) > input", "css:finder"],
        ["xpath=//input[@name='email']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }]
  }, {
    "id": "9759056d-f52c-44a9-8bcd-2e0fa471e7ed",
    "name": "admin",
    "commands": [{
      "id": "1fc87fae-f088-4e7c-9e3c-771e0cdb51ef",
      "comment": "",
      "command": "open",
      "target": "https://carsonpenn.github.io/cse270-teton/admin.html",
      "targets": [],
      "value": ""
    }, {
      "id": "74508554-becb-4a72-ab62-9212376d42ed",
      "comment": "",
      "command": "setWindowSize",
      "target": "1154x1048",
      "targets": [],
      "value": ""
    }, {
      "id": "14a097aa-aa4c-4773-a7fb-6dc26d19ef56",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "7c68c923-b068-404b-80d2-24cf85e29a27",
      "comment": "",
      "command": "type",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": "incorrectUsername"
    }, {
      "id": "81007d19-ed10-4ad8-837d-d5569b4c98ef",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d3fa8f3a-3466-48ac-9d50-1248862c7df6",
      "comment": "",
      "command": "type",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": "incorrectPassowrd"
    }, {
      "id": "f14e9054-4299-4f7a-bf74-b07db3572dcd",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "fbc75026-29dc-413f-90c7-79e4cf952b7f",
      "comment": "",
      "command": "click",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "19ed3a6c-9164-4102-a91b-b835aa8ee07c",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "id=username",
      "targets": [
        ["id=username", "id"],
        ["name=username", "name"],
        ["css=#username", "css:finder"],
        ["xpath=//input[@id='username']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label/input", "xpath:idRelative"],
        ["xpath=//input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "3ae92f18-6958-4913-9a5a-1c9056644642",
      "comment": "",
      "command": "click",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "d6c313bc-07f4-472e-8c05-50ab8ed1c2f2",
      "comment": "",
      "command": "verifyElementPresent",
      "target": "id=password",
      "targets": [
        ["id=password", "id"],
        ["name=password", "name"],
        ["css=#password", "css:finder"],
        ["xpath=//input[@id='password']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/label[2]/input", "xpath:idRelative"],
        ["xpath=//label[2]/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "0cd98e8e-b9f4-4dc9-8dac-646296a7d68f",
      "comment": "",
      "command": "waitForText",
      "target": "css=.admin-main",
      "targets": [
        ["css=.admin-main", "css:finder"],
        ["xpath=//div[@id='content']/main", "xpath:idRelative"],
        ["xpath=//main", "xpath:position"]
      ],
      "value": "Enter Credentials\\nUsername:\\nPassword:"
    }, {
      "id": "f5ed2829-8a6f-495a-bb11-453366426ea9",
      "comment": "",
      "command": "waitForText",
      "target": "css=.admin-main",
      "targets": [
        ["css=.admin-main", "css:finder"],
        ["xpath=//div[@id='content']/main", "xpath:idRelative"],
        ["xpath=//main", "xpath:position"]
      ],
      "value": "Enter Credentials\\nUsername:\\nPassword:"
    }, {
      "id": "11aaaaf3-c1b3-4d0e-bba6-a92d242f6667",
      "comment": "",
      "command": "click",
      "target": "css=.mysubmit:nth-child(4)",
      "targets": [
        ["css=.mysubmit:nth-child(4)", "css:finder"],
        ["xpath=//input[@value='Login']", "xpath:attributes"],
        ["xpath=//div[@id='content']/main/section/form/fieldset/input", "xpath:idRelative"],
        ["xpath=//fieldset/input", "xpath:position"]
      ],
      "value": ""
    }]
  }],
  "suites": [{
    "id": "87848641-ced9-467e-8940-a32af8f04ef3",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": []
  }],
  "urls": ["https://carsonpenn.github.io/", "https://carsonpenn.github.io/cse270-teton/admin.html"],
  "plugins": []
}