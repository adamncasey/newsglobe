var PAGE_NEWS = 'http://localhost/countrynews.json';
var PAGE_COUNTRY_POINTS = 'http://localhost/countrylocations.json';
var PAGE_COUNTRIES = 'http://localhost/countries.json';

function getGlobeData(timestart, callback)
{
	// Get data from server
	getNewsData(function(newsData) {
		console.log(newsData); 
		generateGlobeData(newsData, callback);
	});
}

function generateGlobeData(newsData, callback)
{
	var data = [['SeriesA', []]];
	var offset = 0;
	
	getCountryPoints(function(pointsInCountry) {
		// For each country:
		for(country in newsData)
		{
			console.log(newsData[country]);
			console.log(pointsInCountry[country]);
			produceCountryDataGlobePoints(pointsInCountry[country], newsData[country] / 400.0, data[0][1], offset);
			
			offset += pointsInCountry[country].length * 3;
		}
		
		callback(data);
	});
	
}

function produceCountryDataGlobePoints(countryPoints, newsHeat, array, offset)
{
	var i=0;
	for(point in countryPoints)
	{
		console.log("point: " + countryPoints[point]);
		array[offset + (i*3) + 0] = countryPoints[point][0];
		array[offset + (i*3) + 1] = countryPoints[point][1];
		array[offset + (i*3) + 2] = newsHeat;
		
		console.log("0: " + countryPoints[point][0] + "  1:" + countryPoints[point][1] + "   2: " + newsHeat)
		
		i++;
	}
}

function getNewsData(callback)
{
	// AJAX request from server
	// Expecting format { "countryid": 0-100, ... }
	var xhr = new XMLHttpRequest();
	xhr.open('GET', PAGE_NEWS, false);
	
	xhr.onreadystatechange = function() {
		if(xhr.readyState === 4 && xhr.status === 200)
		{
			var data = JSON.parse(xhr.responseText);
			console.log(xhr.responseText);
			console.log(data);
			
			callback(data);
		}
	};
	xhr.send(null);
}


function getCountryPoints(callback)
{
	// AJAX request from server
	// Expecting format { "countryid": 0-100, ... }
	var xhr = new XMLHttpRequest();
	xhr.open('GET', PAGE_COUNTRY_POINTS, false);
	
	xhr.onreadystatechange = function() {
		if(xhr.readyState === 4 && xhr.status === 200)
		{
			var data = JSON.parse(xhr.responseText);
			console.log(data);
			callback(data);
		}
	};
	
	xhr.send(null);
}
