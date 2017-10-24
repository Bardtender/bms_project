

var timeArray = [];
var dataArray = [];


$(document).ready(function () {

        $('span').click(function() {
            $('.overlay').toggleClass('anim');
        });

        $('.animation').click(function(){
            $('.anim').toggleClass('reverse-animation');
        })
});



function csrfSafeMethod(method) {
			// methods not requiring csrf protection
				return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
			}
			// setup of aja - set headers for csrf
			$.ajaxSetup({
				beforeSend: function(xhr, settings) {
					if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
						xhr.setRequestHeader("X-CSRFToken", csrftoken);
					}
				}
			});
			// ajax request to update graph
			$.ajax({
        		url: 'chart_data/',
        		type:"POST",
        		data: {
          			'action': 'getData',
        		},
        		dataType: 'json',
       			success: function (data) {
       				//if there is new data
          			if (data) {
          				timeArray = data.x;
          				dataArray = data.y;
          				console.log(data.test);
          				//get chart canvas for plotting
            			var ctx = document.getElementById('testChart').getContext('2d');
            			// plot chart.js chart
						var chart = new Chart(ctx, {
    						type: 'line',
    						// format chart data
    						data: {
        						labels: timeArray,
        						datasets: [{
            						label: "example",
            						backgroundColor: 'red',
            						borderColor: 'red',
            						data: dataArray,
            						lineTension: 0,
            						fill: false,
        						}]
    						},

		    				// graph options, set axes etc
    						options: {
    							responsive: true,
    							tooltips: {
    								position: 'nearest',
    								mode: 'index',
    								intersect: false,
    							},
    							scales: {
    								yAxes: [{
    									display: true,
    									scaleLabel: {
    										display: true,
    										labelString: 'temperature'
    									},
    									ticks: {
    										suggestedMin: 10,
    										suggestedMax: 40,
    									}
    								}]
    							}
    						}
						});
          			}
        		}
      		});

        	
		
