/* global Chart */

/**
 * --------------------------------------------------------------------------
 * CoreUI Boostrap Admin Template (v4.2.2): main.js
 * Licensed under MIT (https://coreui.io/license)
 * --------------------------------------------------------------------------
 */

// random Numbers
const random = () => Math.round(Math.random() * 100);
// data
var user_sheets_data =  JSON.parse(document.getElementById('user_sheets_data').dataset.templateVar);
var approved_sheets_data = JSON.parse(document.getElementById('approved_sheets_data').dataset.templateVar);
var unapproved_sheets_data = JSON.parse(document.getElementById('unapproved_sheets_data').dataset.templateVar);

// eslint-disable-next-line no-unused-vars
const lineChart = new Chart(document.getElementById('statics-1'), {
  type: 'line',
  data: {
    labels: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
    datasets: [{
      label: '已审批工单',
      backgroundColor: 'rgba(151, 187, 205, 0.2)',
      borderColor: 'rgba(151, 187, 205, 1)',
      pointBackgroundColor: 'rgba(151, 187, 205, 1)',
      pointBorderColor: '#fff',
      data: approved_sheets_data
    }, {
      label: '未审批工单',
      backgroundColor: 'rgba(220, 220, 220, 0.2)',
      borderColor: 'rgba(220, 220, 220, 1)',
      pointBackgroundColor: 'rgba(220, 220, 220, 1)',
      pointBorderColor: '#fff',
      data: unapproved_sheets_data
    }]
  },
  options: {
    responsive: true
  }
});

const lineChart_2 = new Chart(document.getElementById('statics-2'), {
  type: 'line',
  data: {
    labels: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
    datasets: [{
      label: '工单数',
      backgroundColor: 'rgba(151, 187, 205, 0.2)',
      borderColor: 'rgba(151, 187, 205, 1)',
      pointBackgroundColor: 'rgba(151, 187, 205, 1)',
      pointBorderColor: '#fff',
      data: user_sheets_data
    }, ]
  },
  options: {
    responsive: true
  }
});


const pieChart = new Chart(document.getElementById('dataset-1'), {
  type: 'pie',
  data: {
    labels: ['正常数据', '异常数据'],
    datasets: [{
      data: [4096, 1258],
      backgroundColor: ['#36A2EB', '#CD2626'],
      hoverBackgroundColor: ['#36A2EB', '#CD2626']
    }]
  },
  options: {
    responsive: true
  }
});

const pieChart_2 = new Chart(document.getElementById('dataset-2'), {
  type: 'pie',
  data: {
    labels: ['训练集', '测试集'],
    datasets: [{
      data: [3629, 1725],
      backgroundColor: ['#4169E1', '#FFC125'],
      hoverBackgroundColor: ['#4169E1', '#FFC125']
    }]
  },
  options: {
    responsive: true
  }
});

const polarAreaChart = new Chart(document.getElementById('dataset-3'), {
  type: 'polarArea',
  data: {
    labels: ['地毯', '金属网格', '皮革', '瓷砖', '木板',
     '玻璃瓶底部', '电缆', '胶囊', '榛子', '金属螺母',
      '药丸', '螺丝', '牙刷', '晶体管', '拉链'],
    datasets: [{
      data: [397, 342, 369, 347, 326,
             292, 374, 351, 501, 335, 434, 480, 102, 313, 391],
      backgroundColor: ['#708090', '#E7E9ED', '#FFCE56', '#F5F5DC', '#DEB887',
                        '#2F4F4F', '#483D8B', '#EEB422', '#CD7054', '#C1CDC1',
                        '#D3D3D3', '#BEBEBE', '#FFEFDB', '#EE6363', '#8B8682']
    }]
  },
  options: {
    responsive: true
  }
});

const polarAreaChart_2 = new Chart(document.getElementById('dataset-4'), {
  type: 'polarArea',
  data: {
    labels: ['地毯', '金属网格', '皮革', '瓷砖', '木板',
     '玻璃瓶底部', '电缆', '胶囊', '榛子', '金属螺母', '药丸', '螺丝', '牙刷', '晶体管', '拉链'],
    datasets: [{
      data: [280, 264, 245, 230, 247,
             209, 224, 219, 391, 220, 267, 320, 60, 213, 240],
      backgroundColor: ['#708090', '#E7E9ED', '#FFCE56', '#F5F5DC', '#DEB887',
                        '#2F4F4F', '#483D8B', '#EEB422', '#CD7054', '#C1CDC1',
                        '#D3D3D3', '#BEBEBE', '#FFEFDB', '#EE6363', '#8B8682']
    }]
  },
  options: {
    responsive: true
  }
});

const polarAreaChart_3 = new Chart(document.getElementById('dataset-5'), {
  type: 'polarArea',
  data: {
    labels: ['地毯', '金属网格', '皮革', '瓷砖', '木板',
     '玻璃瓶底部', '电缆', '胶囊', '榛子', '金属螺母', '药丸', '螺丝', '牙刷', '晶体管', '拉链'],
    datasets: [{
      data: [117, 78, 124, 117, 79,
             83, 150, 132, 110, 115, 167, 160, 42, 100, 151],
      backgroundColor: ['#708090', '#E7E9ED', '#FFCE56', '#F5F5DC', '#DEB887',
                        '#2F4F4F', '#483D8B', '#EEB422', '#CD7054', '#C1CDC1',
                        '#D3D3D3', '#BEBEBE', '#FFEFDB', '#EE6363', '#8B8682']
    }]
  },
  options: {
    responsive: true
  }
});

const polarAreaChart_4 = new Chart(document.getElementById('dataset-6'), {
  type: 'polarArea',
  data: {
    labels: ['地毯', '金属网格', '皮革', '瓷砖', '木板',
     '玻璃瓶底部', '电缆', '胶囊', '榛子', '金属螺母', '药丸', '螺丝', '牙刷', '晶体管', '拉链'],
    datasets: [{
      data: [5, 5, 5, 5, 5,
             3, 8, 5, 4, 4, 7, 5, 1, 4, 7],
      backgroundColor: ['#708090', '#E7E9ED', '#FFCE56', '#F5F5DC', '#DEB887',
                        '#2F4F4F', '#483D8B', '#EEB422', '#CD7054', '#C1CDC1',
                        '#D3D3D3', '#BEBEBE', '#FFEFDB', '#EE6363', '#8B8682']
    }]
  },
  options: {
    responsive: true
  }
});
