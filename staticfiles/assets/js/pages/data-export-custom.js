$(document).ready(function() {
    setTimeout(function() {

        // [ HTML5 Export Buttons ]
        $('#basic-btn').DataTable({
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

        // [ Column Selectors ]
        $('#cbtn-selectors').DataTable({
            dom: 'Bfrtip',
            buttons: [{
                extend: 'copyHtml5',
                exportOptions: {
                    columns: [0, ':visible']
                }
            }, {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            },  'colvis']
        });

        // [ Excel - Cell Background ]
        $('#excel-bg').DataTable({
            dom: 'Bfrtip',
            buttons: [{
                extend: 'excelHtml5',
                customize: function(xlsx) {
                    var sheet = xlsx.xl.worksheets['sheet1.xml'];
                    $('row c[r^="F"]', sheet).each(function() {
                        if ($('is t', this).text().replace(/[^\d]/g, '') * 1 >= 500000) {
                            $(this).attr('s', '20');
                        }
                    });
                }
            }]
        });

        // [ Custom File (JSON) ] 
        $('#pdf-json').DataTable({
            dom: 'Bfrtip',
            buttons: [{
                text: 'JSON',
                action: function(e, dt, button, config) {
                    var data = dt.buttons.exportData();
                    $.fn.dataTable.fileSave(new Blob([JSON.stringify(data)]), 'Export.json');
                }
            }]
        });

    }, 350);
});
