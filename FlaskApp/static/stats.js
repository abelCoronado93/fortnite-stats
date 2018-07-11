$(function () {
	var modes = ["solo", "duo", "squad"]
	$('#getStats').click(function () {
		if ($("#username").val() !== "") {
			$.getJSON("/_stats", {
				username: $("#username").val(),
				platform: $("#platform").val()
			},
				function (data) {
					processData(data);
					$(".results").show();
				});
			return false;
		}
		return false;
	});
	function processData(data) {
		$.each(modes, function (key, value) {
			$("#kills-".concat(value)).text(data.stats["kills_".concat(value)]);
			$("#wins-".concat(value)).text(data.stats["placetop1_".concat(value)]);
			$("#matches-".concat(value)).text(data.stats["matchesplayed_".concat(value)]);
			$("#kr-".concat(value)).text(data.stats["kd_".concat(value)]);
			$("#wr-".concat(value)).text(data.stats["winrate_".concat(value)]);
		});
		$("#kills-total").text(data.totals.kills);
		$("#wins-total").text(data.totals.wins);
		$("#matches-total").text(data.totals.matchesplayed);
		$("#kr-total").text(data.totals.kd);
		$("#wr-total").text(data.totals.winrate);
		return false;
	}
});