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
    fetch("task/create/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": "{{ csrf_token }}",
      },
      body: JSON.stringify({ title: taskText, status: 0 }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          const newTask = document.createElement("li");
          newTask.className =
            "list-group-item modern-task d-flex justify-content-between align-items-center";
          newTask.setAttribute("data-task-id", data.task_id);
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
      });
  }
}

function deleteTask(button) {
  const taskItem = button.closest("li");
  const taskId = taskItem.getAttribute("data-task-id");

  fetch(`task/delete/taskId/`.replace("taskId", taskId), {
    method: "DELETE",
    headers: {
      "X-CSRFToken": "{{ csrf_token }}",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        taskItem.remove(); // Remove the task from the DOM
      }
    });
}
// Function to edit a task
function editTask(button) {
  const taskItem = button.closest("li");
  const taskTextElement = taskItem.querySelector(".task-text");
  const taskId = taskItem.getAttribute("data-task-id");

  if (taskItem.classList.contains("editing")) {
    const newText = taskItem.querySelector("input").value.trim();
    if (newText !== "") {
      fetch(`task/update/taskId/`.replace("taskId", taskId), {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": "{{ csrf_token }}",
        },
        body: JSON.stringify({ title: newText }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.success) {
            taskTextElement.textContent = newText; // Update the task text
          }
        });
    }
    taskItem.classList.remove("editing");
    button.innerHTML = '<i class="fas fa-edit"></i>'; // Switch back to the edit icon
  } else {
    const currentText = taskTextElement.textContent;
    taskTextElement.innerHTML = `<input type="text" class="form-control form-control-sm" value="${currentText}">`;
    taskItem.classList.add("editing");
    button.innerHTML = '<i class="fas fa-save"></i>'; // Change icon to "save"
  }
}
function updateTaskStatus(evt) {
  const taskId = evt.item.getAttribute("data-task-id");
  const newStatus = evt.to.id === "todo" ? 0 : evt.to.id === "doing" ? 1 : 2;

  fetch(`task/update/taskId/`.replace("taskId", taskId), {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": "{{ csrf_token }}",
    },
    body: JSON.stringify({ status: newStatus }),
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        console.log(`Task status updated to ${newStatus}`);
      }
    });
}
