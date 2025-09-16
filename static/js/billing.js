 function toggleDropdown() {
      document.getElementById("miniScreen").classList.toggle("show");
    }

    window.onclick = function(event) {
      if (!event.target.matches('.menu-btn')) {
        let dropdowns = document.getElementsByClassName("dropdown");
        for (let i = 0; i < dropdowns.length; i++) {
          let openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }