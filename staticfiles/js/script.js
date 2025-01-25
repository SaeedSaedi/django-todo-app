// Initialize SortableJS for each column
Sortable.create(document.getElementById("todo"), {
  group: "tasks",
  animation: 150,
  onEnd: function (evt) {
    updateTaskStatus(evt);
  },
});

Sortable.create(document.getElementById("doing"), {
  group: "tasks",
  animation: 150,
  onEnd: function (evt) {
    updateTaskStatus(evt);
  },
});

Sortable.create(document.getElementById("done"), {
  group: "tasks",
  animation: 150,
  onEnd: function (evt) {
    updateTaskStatus(evt);
  },
});

// Function to add a new task to the "To Do" column
function addTask() {
  const newTaskInput = document.getElementById("newTask");
  const taskText = newTaskInput.value.trim();

  if (taskText !== "") {
    const newTask = document.createElement("li");
    newTask.className =
      "list-group-item modern-task d-flex justify-content-between align-items-center";
    newTask.innerHTML = `
                <span class="task-text">${taskText}</span>
                <div>
                    <button class="btn btn-sm btn-edit me-1" onclick="editTask(this)">
                        <i class="fas fa-edit"></i>
                    </button>
                    <button class="btn btn-sm btn-delete" onclick="deleteTask(this)">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            `;
    document.getElementById("todo").appendChild(newTask);
    newTaskInput.value = ""; // Clear the input field
  }
}

// Function to delete a task
function deleteTask(button) {
  const taskItem = button.closest("li"); // Get the parent <li> element
  taskItem.remove(); // Remove the task from the DOM
}

// Function to edit a task
function editTask(button) {
  const taskItem = button.closest("li"); // Get the parent <li> element
  const taskTextElement = taskItem.querySelector(".task-text");

  // Check if the task is already in edit mode
  if (taskItem.classList.contains("editing")) {
    const newText = taskItem.querySelector("input").value.trim();
    if (newText !== "") {
      taskTextElement.textContent = newText; // Update the task text
    }
    taskItem.classList.remove("editing");
    button.innerHTML = '<i class="fas fa-edit"></i>'; // Switch back to the edit icon
  } else {
    // Switch to edit mode
    const currentText = taskTextElement.textContent;
    taskTextElement.innerHTML = `<input type="text" class="form-control form-control-sm" value="${currentText}">`;
    taskItem.classList.add("editing");
    button.innerHTML = '<i class="fas fa-save"></i>'; // Change icon to "save"
  }
}

// Function to update task status (optional: you can send this data to the server)
function updateTaskStatus(evt) {
  const taskId = evt.item.textContent.trim();
  const newStatus = evt.to.id; // 'todo', 'doing', or 'done'
  console.log(`Task "${taskId}" moved to ${newStatus}`);
  // You can send this information to the server using AJAX if needed
}
