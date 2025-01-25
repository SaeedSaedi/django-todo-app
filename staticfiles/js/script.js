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
                <span>${taskText}</span>
                <button class="btn btn-sm btn-delete" onclick="deleteTask(this)">
                    <i class="fas fa-trash"></i>
                </button>
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

// Function to update task status (optional: you can send this data to the server)
function updateTaskStatus(evt) {
  const taskId = evt.item.textContent;
  const newStatus = evt.to.id; // 'todo', 'doing', or 'done'
  console.log(`Task "${taskId}" moved to ${newStatus}`);
  // You can send this information to the server using AJAX if needed
}
