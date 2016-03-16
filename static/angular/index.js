var myApp = angular.module('myApp', []);


myApp.controller('gameStoresCtrl', function($scope, $http) 
{
	$http.get('http://localhost:8000/findstore/')
	.then(function(data, status, headers, config)
	{
		$scope.gameStores = []
		for (var x = 0; x < data.data.length; x++)
		{
			console.log(data.data[x].fields)
			$scope.gameStores[x] = data.data[x].fields.name
		}
		// console.log(data.data)
		// $scope.gameStores = data.data;
		
	});
});

myApp.controller('sessionsCtrl', function($scope, $http) 
{
	$http.get('http://localhost:8000/storeview/')
	.then(function(data, status, headers, config)
	{
		console.log(data)
		$scope.gameStores = data;
		
	});
});