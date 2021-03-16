'use strict';
$(document).ready(function() {
	setTimeout(function() {
		$(function() {
			var options = {
				chart: {
					height: 360,
					type: 'donut',
				},

				labels: ['Programing Skills', 'Soft Skills', 'Analytical Skills'],
				series: [70, 20, 10],
				colors: ["#00bcd4", "#FFB64D", "#FF5370"],
				legend: {
					show: true,
					position: 'bottom',
					fontSize: '14px',
				},
				fill: {
					type: 'solid',
					gradient: {
						shade: 'light',
						
					}
				},
				dataLabels: {
					enabled: true,
					formatter: function(val) {
						return Math.floor(val) + "%";
					},
					dropShadow: {
						enabled: false,
					},

				},
				plotOptions: {
					pie: {
						donut: {
							labels: {
								show: true,
								name: {
									show: true
								},
								value: {
									show: true,
									formatter: function(val) {
										return Math.floor(val) + "%";
									},
								},
								
							}
						}
					}
				},
				responsive: [{
					breakpoint: 480,
					options: {
						legend: {
							position: 'bottom'
						}
					}
				}]
			}
			var chart = new ApexCharts(
				document.querySelector("#pie-chart"),
				options
			);
			chart.render();
		});
		
	
	}, 700);
});
