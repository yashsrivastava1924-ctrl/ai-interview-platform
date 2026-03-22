const token = localStorage.getItem("token");

async function loadData() {
  // user
  const userRes = await fetch("http://localhost:5000/api/users/me", {
    headers: { Authorization: token }
  });
  const user = await userRes.json();

  document.getElementById("username").innerText = user.name;
  document.getElementById("points").innerText = user.points;

  // leaderboard
  const res = await fetch("http://localhost:5000/api/users/leaderboard");
  const data = await res.json();

  const list = document.getElementById("leaderboard");

  data.forEach((u, i) => {
    const li = document.createElement("li");
    li.innerText = `${i+1}. ${u.name} - ${u.points}`;
    list.appendChild(li);
  });
}

loadData();