/* global Chart */

/**
 * --------------------------------------------------------------------------
 * CoreUI Boostrap Admin Template (v4.2.2): main.js
 * Licensed under MIT (https://coreui.io/license)
 * --------------------------------------------------------------------------
 */

// random Numbers
const random = () => Math.round(Math.random() * 100);

// eslint-disable-next-line no-unused-vars
const lineChart = new Chart(document.getElementById('canvas-1'), {
  type: 'line',
  data: {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [{
      label: 'My First dataset',
      backgroundColor: 'rgba(220, 220, 220, 0.2)',
      borderColor: 'rgba(220, 220, 220, 1)',
      pointBackgroundColor: 'rgba(220, 220, 220, 1)',
      pointBorderColor: '#fff',
      data: [random(), random(), random(), random(), random(), random(), random()]
    }, {
      label: 'My Second dataset',
      backgroundColor: 'rgba(151, 187, 205, 0.2)',
      borderColor: 'rgba(151, 187, 205, 1)',
      pointBackgroundColor: 'rgba(151, 187, 205, 1)',
      pointBorderColor: '#fff',
      data: [random(), random(), random(), random(), random(), random(), random()]
    }]
  },
  options: {
    responsive: true
  }
});

const polarAreaChart = new Chart(document.getElementById('canvas-3'), {
  type: 'polarArea',
  data: {
    labels: ['正常数据', '无效数据', '广告数据'],
    datasets: [{
      data: [1854, 204, 839],
      backgroundColor: ['#FF6384', '#E7E9ED', '#FFCE56']
    }]
  },
  options: {
    responsive: true
  }
});

const pieChart = new Chart(document.getElementById('canvas-4'), {
  type: 'pie',
  data: {
    labels: ['广告数据', '非广告数据'],
    datasets: [{
      data: [516, 514],
      backgroundColor: ['#FFCE56', '#36A2EB'],
      hoverBackgroundColor: ['#FFCE56', '#36A2EB']
    }]
  },
  options: {
    responsive: true
  }
});


//# sourceMappingURL=charts.js.map
