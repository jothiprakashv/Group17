$(document).ready(function() {
	setTimeout(function() {
		// [ Zero Configuration ] start
		$('#simpletable').DataTable();
		$('#simpletable2').DataTable({
			dom: 'Bfrtip',

			buttons: ['copy','print',{
				extend: 'collection',
				text: 'Export as',
				buttons: [ 
				{
					extend: 'csv',
					text: '<i class="text-info feather icon-file" ></i> csv',
				},
				{
					extend: 'excel',
					text: '<i class="text-info feather icon-file" ></i> excel',
				},
				{
					text: '<i class="text-info feather icon-file-text" ></i> JSON',
					action: function(e, dt, button, config) {
						var data = dt.buttons.exportData();
						$.fn.dataTable.fileSave(new Blob([JSON.stringify(data)]), 'Export.json');
					}
				}

				]
			}]
		});
		$('#simpletable3').DataTable({
			dom: 'Bfrtip',
			buttons: ['copy','print',{
				extend: 'collection',
				text: 'Export as',
				buttons: [ 
				{
					extend: 'csv',
					text: '<i class="text-info feather icon-file" ></i> csv',
				},
				{
					extend: 'excel',
					text: '<i class="text-info feather icon-file" ></i> excel',
				},
				{
					text: '<i class="text-info feather icon-file-text" ></i> JSON',
					action: function(e, dt, button, config) {
						var data = dt.buttons.exportData();
						$.fn.dataTable.fileSave(new Blob([JSON.stringify(data)]), 'Export.json');
					}
				}

				]
			}]
		});

		// [ Default Ordering ] start
		$('#order-table').DataTable({
			"order": [
				[3, "desc"]
			]
		});

		// [ Multi-Column Ordering ]
		$('#multi-colum-dt').DataTable({
			columnDefs: [{
				targets: [0],
				orderData: [0, 1]
			}, {
				targets: [1],
				orderData: [1, 0]
			}, {
				targets: [4],
				orderData: [4, 0]
			}]
		});

		// [ Complex Headers ]
		$('#complex-dt').DataTable();

		// [ DOM Positioning ]
		$('#DOM-dt').DataTable({
			"dom": '<"top"i>rt<"bottom"flp><"clear">'
		});

		// [ Alternative Pagination ]
		$('#alt-pg-dt').DataTable({
			"pagingType": "full_numbers"
		});

		// [ Scroll - Vertical ]
		$('#scr-vrt-dt').DataTable({
			"scrollY": "200px",
			"scrollCollapse": true,
			"paging": false
		});

		// [ Scroll - Vertical, Dynamic Height ]
		$('#scr-vtr-dynamic').DataTable({
			scrollY: '50vh',
			scrollCollapse: true,
			paging: false
		});

		// [ Language - Comma Decimal Place ]
		$('#lang-dt').DataTable({
			"language": {
				"decimal": ",",
				"thousands": "."
			}
		});

	}, 350);
});
