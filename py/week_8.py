def radio_stations():
    states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
    stations = {
        'kone': {'id', 'nv', 'ut'},
        'ktwo': {'wa', 'id', 'mt'},
        'kthree': {'or', 'nv', 'ca'},
        'kfour': {'nv', 'ut'},
        'kfive': {'ca', 'az'}
    }
    final_stations = set()

    while states_needed:
        best_station = None
        state_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(state_covered):
                best_station = station
                state_covered = covered
        states_needed -= state_covered
        final_stations.add(best_station)
        del stations[best_station]

    print(final_stations)


if __name__ == '__main__':
    radio_stations()
