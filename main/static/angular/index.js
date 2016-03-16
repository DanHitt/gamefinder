var myApp = angular.module('myApp', []);


myApp.controller('gameStoresCtrl', function($scope, $http) 
{
	$http.get('http://localhost:8000/findstore/')
	.then(function(data, status, headers, config)
	{
		console.log(status)
		$scope.gameStores = []
		for (var x = 0; x < data.data.length; x++)
		{
			console.log(data.data[x].fields)
			$scope.gameStores[x] = data.data[x]
			$scope.clickMe = false;
    	$scope.clickMeFunc = function() 
    	{
        	$scope.clickMe = !$scope.clickMe;
        }

		}		





		var addSession = function(j)
		{
			$http.get('http://localhost:8000/storeview/'+j)
			.then(function(data, status, headers, config)
			{
				$scope.sessions = []
				for (var x = 0; x < data.data.length; x++)
				{
					console.log(data.data[x].fields)
					if (data.data[x].fields.game_store === j)
					{
						$scope.sessions[x] = data.data[x]
					}
				}

				
			});
		}
		for (var j=1; j <= data.data.length; j++)
		{
			addSession(j)
		}
	});
});

