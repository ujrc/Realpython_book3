// var pollsApp = angular.module('pollsApp', []);
//
// pollsApp.config(function($interpolateProvider) {
//   $interpolateProvider.startSymbol('[[')
//     .endSymbol(']]');
// });
mecApp.controller('UserPollCtrl', function($scope, pollFactory) {
  //get the Poll
  $scope.poll = ""

  function setPoll(promise) {
    $scope.poll = promise;
  }

  function getPoll() {
    return pollFactory.getPoll(1);
  }

  $scope.barcolor = function(i) {
    var colors = ['progress-bar-success', 'progress-bar-info',
      'progress-bar-warning', 'progress-bar-danger', ''
    ]
    var idx = i % colors.length;
    return colors[idx];
  }
  getPoll().then(setPoll);

  $scope.vote = function(item) {
    pollFactory.vote_for_item(item)
      .then(getPoll)
      .then(setPoll);
  }

});
mecApp.factory('pollFactory', function($http,$filter) {

  var baseUrl = '/api/v1/';
  var pollUrl = baseUrl + 'polls/';
  var pollItemUrl = baseUrl + 'poll_items/';
  var pollId=0;
  var pollFactory = {};

  pollFactory.getpoll = function() {
    var tempUrl=pollUrl;
    if(pollId !=0){tempUrl=pollUrl+pollId;}

    return $http.get(pollUrl).then(function(response){
      var latestPoll=$filter('orderBy')(response.data,'-publish_date')[0];
    pollId=latestPoll.id;
  return latestPoll;
});
};

  pollFactory.vote_for_item = function(poll_item) {
    poll_item.votes += 1;
    return $http.put(pollItemsUrl + poll_item.id, poll_item);
  }
  return pollFactory;
});

// pollsApp.factory('pollFactory', function($http) {
//   var baseUrl = '/api/v1/';
//   var pollUrl = baseUrl + 'polls/';
//   var pollItemsUrl = baseUrl + 'poll_items/';
//
//   var pollFactory = {};
//
//   pollFactory.getPoll = function(id) {
//     return $http.get(pollUrl + id);
//   };
//
//   pollFactory.vote_for_item = function(poll_item) {
//     poll_item.votes += 1;
//     return $http.put(pollItemsUrl + poll_item.id, poll_item);
//   }
//
//   return pollFactory;
// });

pollsApp.controller('UserPollCtrl', function($scope, pollFactory) {

//get the Poll
$scope.poll = ""

function setPoll(promise) {
  $scope.poll = promise.data;
}

function getPoll() {
  return pollFactory.getPoll(1);
}

$scope.barcolor = function(i) {
  var colors = ['progress-bar-success', 'progress-bar-info',
    'progress-bar-warning', 'progress-bar-danger', ''
  ]
  var idx = i % colors.length;
  return colors[idx];
}

getPoll().then(setPoll);

$scope.vote = function(item) {
  pollFactory.vote_for_item(item)
    .then(getPoll)
    .then(setPoll);
}
});


// pollsApp.controller('UserPollCtrl', function($scope, $http) {
//       // Get the Poll
//       $scope.poll = ""
//
//       $http.get('/api/v1/polls/1').
//       success(function(data) {
//         $scope.poll = data;
//       }).
//       error(function(data, status) {
//         console.log("calling /api/v1/polls/1 returned status " +
//           status);
//       });
//       $scope.barcolor = function(i) {
//         colors = ['progress-bar-success', 'progress-bar-info',
//           'progress-bar-warning', 'progress-bar-danger', ''
//         ]
//         idx = i % colors.length;
//         return colors[idx];
//       }
//       $scope.total_votes = 0;
//       $scope.vote = function(item) {
//         item.votes += 1;
//         $http.put('/api/v1/poll_items/' + item.id, item).success(function(data) {
//           $http.get('/api/v1/polls/1').success(function(data) {
//             $scope.poll = data;
//           }).error(function(data, status) {
//             console.log("calling /api/v1/polls/1 returned status " + status);
//           });
//         }).error(function(data, status) {
//           console.error("calling PUT /api/v1/poll_items returned status " + status);
//         });

// $scope.total_votes = 0;
// $scope.vote=function(item){
//   item.votes=item.votes+1;
//   $scope.total_votes=$scop.total_votes+1;
//   for (i in $scope.poll.items){
//     var temp_item=$scope.poll.items[i];
//     temp_item.percentage=temp_item.votes/$scope.total_votes*100;
//   }
// };
// $scope.vote_data = {}
// $scope.vote = function(voteModel) {
//   if (!$scope.vote_data.hasOwnProperty(voteModel)) {
//     $scope.vote_data[voteModel] = {
//       "votes": 0,
//       "percent": 0
//     };
//     $scope[voteModel] = $scope.vote_data[voteModel];
//   }
//   $scope.vote_data[voteModel]["votes"] =
//     $scope.vote_data[voteModel]["votes"] + 1;
//   $scope.total_votes = $scope.total_votes + 1;
//   for (var key in $scope.vote_data) {
//     var item = $scope.vote_data[key];
//     item["percent"] = item["votes"] / $scope.total_votes * 100;
//   }
// };
});
