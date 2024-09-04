// Get references to the news boxes and their lists
const newsBox1 = document.getElementById('news-list-1');
const newsBox2 = document.getElementById('news-list-2');

// Function to add news items to a specific news box
function addNewsItem(newsBox, title, content) {
  const listItem = document.createElement('li');
  listItem.innerHTML = `<strong>${title}</strong><br>${content}`; // Format the news item with title and content
  newsBox.appendChild(listItem);
}

// Sample news items (replace with your actual data)
const newNews1 = {
  title: "New Coal Mine Discovered",
  content: "A significant new coal mine has been found in the state of Jharkhand."
};

const newNews2 = {
  title: "Coal Production Reaches New High",
  content: "India's coal production has surpassed all previous records."
};

// Add the sample news items to the boxes
addNewsItem(newsBox1, newNews1.title, newNews1.content);
addNewsItem(newsBox2, newNews2.title, newNews2.content);

// Function to fetch news data from an API (replace with your actual API call)
function fetchNewsData() {
  // Simulate fetching data (replace with your actual API call)
  const simulatedData = [
    { title: "Coal Prices Rise", content: "Global coal prices have increased due to rising demand." },
    { title: "Government Launches New Coal Initiative", content: "The government has announced a new initiative to promote sustainable coal mining." }
  ];

  // Add the fetched news items to the boxes
  simulatedData.forEach(newsItem => {
    addNewsItem(newsBox1, newsItem.title, newsItem.content);
  });
}

// Call the fetchNewsData function to retrieve and display news
fetchNewsData();

// Function to automatically scroll the news boxes
function autoScrollNewsBoxes() {
  const scrollHeight1 = newsBox1.scrollHeight;
  const scrollHeight2 = newsBox2.scrollHeight;
  const scrollTop1 = newsBox1.scrollTop;
  const scrollTop2 = newsBox2.scrollTop;
  const clientHeight1 = newsBox1.clientHeight;
  const clientHeight2 = newsBox2.clientHeight;

  // Check if the scroll position is near the bottom of the box
  if (scrollTop1 + clientHeight1 >= scrollHeight1 - 10) {
    newsBox1.scrollTop = 0; // Scroll back to the top
  } else {
    newsBox1.scrollTop += 1; // Scroll down by 1 pixel
  }

  if (scrollTop2 + clientHeight2 >= scrollHeight2 - 10) {
    newsBox2.scrollTop = 0; // Scroll back to the top
  } else {
    newsBox2.scrollTop += 1; // Scroll down by 1 pixel
  }
}

// Call the autoScrollNewsBoxes function every 100 milliseconds (adjust as needed)
setInterval(autoScrollNewsBoxes, 100);

// Get references to the chart containers
const productionChartContainer = document.getElementById('productionChart');
const emissionsChartContainer = document.getElementById('emissionsChart');

// Create the charts
const productionChart = new Chart(productionChartContainer, {
  type: 'bar',
  data: {
    labels: ['2018', '2019', '2020', '2021', '2022'],
    datasets: [{
      label: 'Coal Production (Million Tonnes)',
      data: [700, 750, 800, 850, 900],
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgba(255, 99, 132, 1)',
      borderWidth: 1
    }]
  },
  options: {
    title: {
      display: true,
      text: 'Coal Production Statistics'
    },
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

const emissionsChart = new Chart(emissionsChartContainer, {
  type: 'line',
  data: {
    labels: ['2018', '2019', '2020', '2021', '2022'],
    datasets: [{
      label: 'CO2 Emissions (Million Tonnes)',
      data: [400, 420, 440, 460, 480],
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgba(54, 162, 235, 1)',
      borderWidth: 1
    }]
  },
  options: {
    title: {
      display: true,
      text: 'CO2 Emissions Statistics'
    },
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});