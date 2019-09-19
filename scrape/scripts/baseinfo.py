# Base information for loading into database

organisations = [
    {
        "orgName": "Napier City Council",
        "shortName": "NCC"
    },
    {
        "orgName": "Hastings District Council",
        "shortName": "HDC"
    },
    {
        "orgName": "Central Hawke's Bay District Council",
        "shortName": "CHBDC"
    },
    {
        "orgName": "Hawke's Bay Regional Council",
        "shortName": "HBRC"
    },
    {
        "orgName": "Wairoa District Council",
        "shortName": "WDC"
    },
    {
        "orgName": "Hawke's Bay District Health Board",
        "shortName": "HBDHB"
    }
]

representatives = [
    {
        "orgShortName": "HDC",
        "fromDate": "",
        "toDate": "",
        "reps": [
            {
                "Surname": "Hazlehurst",
                "Forename": "Sandra",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/SandraHazlehurst-HDCweb.jpg"
            },
            {
                "Surname": "Kerr",
                "Forename": "Tania",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/TaniaKerr-HDCweb.jpg"
            },
            {
                "Surname": "Barber",
                "Forename": "Bayden",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/BaydenBarber-HDCweb.jpg"
            },
            {
                "Surname": "Dixon",
                "Forename": "Malcolm",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/MalcolmDixon-HDCweb.jpg"
            },
            {
                "Surname": "Harvey",
                "Forename": "Damon",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/DamonHarvey-HDCweb.jpg"
            },
            {
                "Surname": "Heaps",
                "Forename": "Rod",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/RodHeaps-HDCweb.jpg"
            },
            {
                "Surname": "Lawson",
                "Forename": "Eileen",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/EileenLawson-HDCweb.jpg"
            },
            {
                "Surname": "Lyons",
                "Forename": "George",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/GeorgeLyons-HDCweb.jpg"
            },
            {
                "Surname": "Nixon",
                "Forename": "Simon",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/SimonNixon-HDCweb.jpg"
            },
            {
                "Surname": "O'Keefe",
                "Forename": "Henare",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/HenareOkeefe-HDCweb.jpg"
            },
            {
                "Surname": "Poulain",
                "Forename": "Jacoby",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/JacobyPoulain-HDCweb.jpg"
            },
            {
                "Surname": "Redstone",
                "Forename": "Ann",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/AnnRedstone-HDCweb.jpg"
            },
            {
                "Surname": "Schollum",
                "Forename": "Wendy",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/WendySchollum-HDCweb.jpg"
            },
            {
                "Surname": "Travers",
                "Forename": "Geraldine",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/GeraldineTravers-HDCweb.jpg"
            },
            {
                "Surname": "Watkins",
                "Forename": "Kevin",
                "ImageUrl": "https://www.hastingsdc.govt.nz/assets/Contacts/KevinWatkins-HDCweb.jpg"
            }
        ]
    }
]

meetingUrl = [
    {
        "org_short": "HDC",
        "meet_sched_url": "http://hastings.infocouncil.biz/"
    },
    {
        "org_short": "NCC",
        "meet_sched_url": "http://napier.infocouncil.biz/"
    }
]

meetingTypeScrapeHelp = [
    {
        "org_short": "HDC",
        "meet_type": "Council",
        "startWord": "present:",
        "endWord": "attendance:"
    }
]

# Meeting types that all councillors are expected to attend
meetingRepAll = [
    {
        "org_short": "HDC",
        "meet_type": "Council"
    }
]
