var myApp = angular.module('myApp', []);


myApp.controller('gameStoresCtrl', function($scope, $http) 
{
	$http.get('http://localhost:8000/findstore/')
	.then(function(data, status, headers, config)
	{
		console.log(data)
		$scope.gameStores = data;
		
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