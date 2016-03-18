var myApp = angular.module('myApp', []);


myApp.controller('gameStoresCtrl', function($scope, $http) 
{
	$http.get('http://localhost:8000/findstore/')
	.then(function(data, status, headers, config)
	{

		gameStores = []
		temp_sessions = []
		for (var x = 0; x < data.data.length; x++)
		{
			if (data.data[x].model == "main.gamestore")
			{
				gameStores.push(data.data[x])


				$scope.clickMe = false;

      } 
      else if (data.data[x].model == "main.session")
      {
      	temp_sessions.push(data.data[x])
      }
		}		


		for (var x = 0; x < gameStores.length; x++)
		{
			gameStores[x].fields.sessions = []
			for (var j = 0; j < temp_sessions.length; j++)
			{
				console.log(temp_sessions[j])
				if (gameStores[x].pk == temp_sessions[j].fields.game_store)
				{
					console.log(gameStores.fields)
					gameStores[x].fields.sessions.push(temp_sessions[j])
				}
			}
		}
	$scope.gameStores = gameStores
	});
});

// track by $index