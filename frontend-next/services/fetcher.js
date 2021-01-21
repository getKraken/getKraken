import axios from 'axios';

export async function fetchAll(web=true) {
  if (web) {
    return webFetchAll();
  }else {
    return mockFetchAll();
  }
}

export async function fetchOne(id, web=true) {
  if (web) {
    return webFetchOne(id);
  } else {
    return mockFetchOne(id);
  }
}

function mockFetchAll() {
  return [
      {'id': 1, 'title':'kraken-season-2021', 'organizer':'paul','participants':['yoni','paul','will','mark']},
      {'id': 2, 'title':'shabbat-winter-2021', 'organizer':'yoni','participants':['yoni','paul','will','mark']},
      {'id': 3, 'title':'operah-winter-2021', 'organizer':'will','participants':['yoni','paul','will','mark']},
      {'id': 4, 'title':'seahawks-season-2021', 'organizer':'mark','participants':['yoni','paul','will','mark']},
  ]
}

function mockFetchOne(id) {
  const series = mockFetchAll();
  for(let singleSeries of series) {
    if (singleSeries.id == id) {
      return series;
    }
  }
  return null;
}

async function webFetchAll(user) {
  //TODO: replace the filler base with the actual url for our deployed backend
  const base = 'heroku backend deployment url'

  try {
    const tokenResponse = await axios.post(base + '/api/token/', {
      username: `${user.username}`
    })
  }

}