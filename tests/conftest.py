import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

INITIAL_ACTIVITIES = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"],
    },
    "Soccer Team": {
        "description": "Team training and matches for students who love soccer",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["nina@mergington.edu", "liam@mergington.edu"],
    },
    "Basketball Club": {
        "description": "Practice basketball skills and compete in friendly games",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["alex@mergington.edu", "zoe@mergington.edu"],
    },
    "Art Club": {
        "description": "Explore drawing, painting, and other visual arts",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["sara@mergington.edu", "miles@mergington.edu"],
    },
    "Drama Club": {
        "description": "Rehearse scenes and perform theatrical productions",
        "schedule": "Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 20,
        "participants": ["julia@mergington.edu", "ben@mergington.edu"],
    },
    "Science Olympiad": {
        "description": "Prepare for science competitions and engage in experiments",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": ["maya@mergington.edu", "kevin@mergington.edu"],
    },
    "Debate Team": {
        "description": "Build argument skills and compete in debate tournaments",
        "schedule": "Tuesdays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["nora@mergington.edu", "ethan@mergington.edu"],
    },
}


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities = copy.deepcopy(INITIAL_ACTIVITIES)


@pytest.fixture
def client(reset_activities):
    return TestClient(app_module.app)
