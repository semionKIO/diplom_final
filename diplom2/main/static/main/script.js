let sidebarToggle = document.getElementById('sidebar-toggle');
let sidebar = document.querySelector('.sidebar');

sidebarToggle.addEventListener('click', function() {
  toggleSidebar();
});

document.addEventListener('click', function(e) {
  if (!sidebar.contains(e.target) && !sidebarToggle.contains(e.target)) {
    sidebar.style.left = '-200px';
  }
});

function toggleSidebar() {
  if (sidebar.style.left === '-200px') {
    sidebar.style.left = '0';
  } else {
    sidebar.style.left = '-200px';
  }
}

let openModalBtn = document.getElementById('open-modal');
let modal = document.getElementById('modal');
let closeModalBtn = document.getElementsByClassName('close')[0];

openModalBtn.addEventListener('click', function() {
  modal.style.display = 'block';
});

closeModalBtn.addEventListener('click', function() {
  modal.style.display = 'none';
});

window.addEventListener('click', function(e) {
  if (e.target == modal) {
    modal.style.display = 'none';
  }
});


