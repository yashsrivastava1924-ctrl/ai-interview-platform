const token = localStorage.getItem("token");

// Get user
async function getUser() {
  const res = await fetch("http://localhost:5000/api/users/me", {
    headers: { Authorization: token }
  });

  const user = await res.json();

  document.getElementById("username").innerText = "Welcome " + user.name;
  document.getElementById("points").innerText = "Points: " + user.points;
}

// Leaderboard
async function getLeaderboard() {
  const res = await fetch("http://localhost:5000/api/users/leaderboard");
  const data = await res.json();

  const list = document.getElementById("leaderboard");

  data.forEach((u, i) => {
    const li = document.createElement("li");
    li.innerText = `${i+1}. ${u.name} - ${u.points}`;
    list.appendChild(li);
  });
}

// Button
function startPractice() {
  alert("Practice module coming next 🚀");
}

// load
getUser();
getLeaderboard();