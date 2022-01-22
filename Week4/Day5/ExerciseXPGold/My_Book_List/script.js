class Book{
    constructor(title, author, image, alreadyRead){
        this.title = title;
        this.author = author;
        this.image = image;
        this.alreadyRead = alreadyRead;
    }
}

allBooks = [];
allBooks[0] = new Book("The Jungle Book", "Rudyard Kipling", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/JunglebookCover.jpg/220px-JunglebookCover.jpg", true);
allBooks[1] = new Book("The Three Musketeers", "Alexandre Dumas", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Dartagnan-musketeers.jpg/220px-Dartagnan-musketeers.jpg", true);
allBooks[2] = new Book("The White Fang", "Jack London", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/JackLondonwhitefang1.jpg/220px-JackLondonwhitefang1.jpg", true);
allBooks[3] = new Book("The Grapes of Wrath", "John Steinbeck", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/The_Grapes_of_Wrath_%281939_1st_ed_cover%29.jpg/220px-The_Grapes_of_Wrath_%281939_1st_ed_cover%29.jpg", false);

let table = document.createElement("table");
document.getElementsByClassName("listBooks")[0].appendChild(table);

for (currentBook of allBooks){
    let row = document.createElement("tr");
    table.appendChild(row);
    let bookHeader = document.createElement("td");
    bookHeader.innerHTML = "<p>" + currentBook.title + " by " + currentBook.author + "</p>";
    let bookImageData = document.createElement("td");
    let bookImageURL = document.createElement("img");
    bookImageURL.setAttribute("src", currentBook.image);
    bookImageURL.setAttribute("style", "width:100px;");
    bookImageData.appendChild(bookImageURL);
    row.appendChild(bookHeader);
    row.appendChild(bookImageData);

    if (currentBook.alreadyRead)
        bookHeader.firstElementChild.setAttribute("style", "color: RGB(200, 80, 101);");
}

