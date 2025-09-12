async function loadChart() {
      const response = await fetch("/chart-data");
      const data = await response.json();

      const ctx = document.getElementById("myPieChart").getContext("2d");
      new Chart(ctx, {
        type: "pie",
        data: {
          labels: data.labels,
          datasets: [{
            data: data.values,
            backgroundColor: [
              "rgba(255, 99, 132, 0.6)",
              "rgba(54, 162, 235, 0.6)",
              "rgba(255, 206, 86, 0.6)",
              "rgba(75, 192, 192, 0.6)",
              "rgba(153, 102, 255, 0.6)",
              "rgba(255, 159, 64, 0.6)"
            ]
          }]
        }
      });
    }

    loadChart();