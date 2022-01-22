function createCalendar(year, month) {
    // Removing old table
    // console.log(typeof(document.body));
    let tableMonth = document.getElementsByTagName("table")[0];
    if (tableMonth)
        tableMonth.remove();
    // Creating table with caption
    tableMonth = document.createElement("table");
    let caption = document.createElement("caption");
    caption.innerText = year + " " + month.replace(/^\w/, (c) => c.toUpperCase());
    document.body.appendChild(tableMonth);
    tableMonth.setAttribute("style", "margin: 20px; border: 1px solid; border-spacing: 0;")
    tableMonth.appendChild(caption);
    // Creating header of table
    let tableHead = document.createElement("thead");//head
    tableMonth.appendChild(tableHead);
    let row = document.createElement("tr");//head
    row.appendChild(document.createElement("th")).innerText = "MO";
    row.appendChild(document.createElement("th")).innerText = "TU";
    row.appendChild(document.createElement("th")).innerText = "WE";
    row.appendChild(document.createElement("th")).innerText = "TH";
    row.appendChild(document.createElement("th")).innerText = "FR";
    row.appendChild(document.createElement("th")).innerText = "SA";
    row.appendChild(document.createElement("th")).innerText = "SU";
    tableHead.appendChild(row);

    //creating body of table
    let tableBody = document.createElement("tbody");
    tableMonth.appendChild(tableBody);

    let firstDay = new Date(`${month} 1, ${year}`);
    firstDay = (firstDay.getDay() + 6) % 7;
    let dayCounter = 1;
    const daysInMonth = getDaysInMonth(year, month);
    for (let y = 0; y < 6; y++) {
        row = document.createElement("tr");

        for (let x = 0; x < 7; x++) {
            let data = document.createElement("td")
            row.appendChild(data);
            if ((y > 0 || x >= firstDay) && (dayCounter <= daysInMonth))
                data.innerText = dayCounter++;
        }
        tableBody.appendChild(row);
    }
    document.querySelectorAll("tr").forEach((row, index) => {
        if (index % 2)
            row.setAttribute("style", "background-color: lightgray;");
    });
}


function getDaysInMonth(year, month) {
    daysInMonthList = {
        "january": 31,
        "february": 28 + !(year % 4) - !(year % 100) + !(year % 400),
        "march": 31,
        "april": 30,
        "may": 31,
        "june": 30,
        "july": 31,
        "august": 31,
        "september": 30,
        "october": 31,
        "november": 30,
        "december": 31
    }
    return daysInMonthList[month];
}

