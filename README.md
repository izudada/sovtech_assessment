`
    query fetchAllPersons {
        persons(page: "4") {
            success
            errors
            persons {
            name
            height
            mass
            gender
            homeworld
            }
        }
    }
`