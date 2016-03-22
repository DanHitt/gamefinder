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


				$scope.showSessions = false;
				$scope.showPlayers = false;

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


	$http.get('http://localhost:8000/players/')
	.then(function(data,status,headers,config)
	{
		$scope.players = []
		for (var n = 0; n < data.data.length; n++)
		{
			$scope.players.push(data.data[n])
			console.log($scope.players)
		}
	})	
}); //myApp.controller


//*******************
var substringMatcher = function(strs) {
  return function findMatches(q, cb) {
    var matches, substringRegex;

    // an array that will be populated with substring matches
    matches = [];
    $scope.checkState = ''

    // regex used to determine if a string contains the substring `q`
    substrRegex = new RegExp(q, 'i');

    // iterate through the pool of strings and for any string that
    // contains the substring `q`, add it to the `matches` array
    $.each(strs, function(i, str) {
      if (substrRegex.test(str)) {
        matches.push(str);
      }
    });

    cb(matches);
  };
};

var states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
  'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii',
  'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
  'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
  'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
  'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota',
  'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island',
  'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
  'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
];

$('#the-basics .typeahead').typeahead({
  hint: true,
  highlight: true,
  minLength: 1
},
{
  name: 'states',
  source: substringMatcher(states)
});


