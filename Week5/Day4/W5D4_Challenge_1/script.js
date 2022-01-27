let listTasks = [];

class Record {
    constructor(text, index) {
        this.done = false;
        this.text = text;
        this.id = index;
        this.container = document.createElement("div");
        this.container.setAttribute("class", "d-flex border-bottom border-2 border-black-50 m-0");

        this.delButton = document.createElement("i");
        this.delButton.setAttribute("class", "m-2 fa fa-window-close");
        this.delButton.setAttribute("style", "color: red;");
        this.delButton.addEventListener("click", removeTask);
        this.container.appendChild(this.delButton);

        this.checkbox = document.createElement("input");
        this.checkbox.setAttribute("id", `${index}`);
        this.checkbox.setAttribute("type", "checkbox");
        this.checkbox.setAttribute("class", "form-check-input m-2");
        this.container.appendChild(this.checkbox);

        this.label = document.createElement("label");
        this.label.setAttribute("class", "text-start m-1 ps-2");
        this.label.setAttribute("for", `${index}`);
        this.label.innerText = text;
        this.container.appendChild(this.label);
        this.checkbox.addEventListener("change", taskComplete);
    }
}

/*
 * Create new object of record and push it to array listTasks 
 */
function addTask() {
    let caption = document.getElementById("newTask").value;
    if (caption != "") {
        let rec = new Record(caption, listTasks.length);
        document.getElementById("listTasks").prepend(rec.container);
        document.getElementById("newTask").value = "";
        listTasks.push(rec);
    }
}

/*
 * Erase all records
 */
function clearAll() {
    listTasks = [];
    document.getElementById("listTasks").innerHTML = "";
}

/*
 *  apply crossline and "done" property on completed task
 */
function taskComplete() {
    id = this.id;
    listTasks[id].done = !listTasks[id].done
    if (listTasks[id].done)
        listTasks[id].label.setAttribute("style", "text-decoration: line-through;");
    else
        listTasks[id].label.setAttribute("style", "text-decoration: none;");
    refreshList(listTasks);
}

/*
 * remove record
 */
function removeTask() {
    id = this.parentElement.getElementsByTagName("input")[0].id;
    listTasks.splice(id, 1);
    refreshList(listTasks);
}

/*
 * Clear all list and print it 
 */
function refreshList(listTasks) {
    document.getElementById("listTasks").innerHTML = "";
    for (index in listTasks) {
        listTasks[index].id = index;
        listTasks[index].checkbox.setAttribute("id", `${index}`);
        listTasks[index].label.setAttribute("for", `${index}`);
        document.getElementById("listTasks").prepend(listTasks[index].container);
    }
}