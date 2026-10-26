def trim_transient_process(data_list, start_idx, end_idx):
    return data_list[start_idx:end_idx]

def calculate_channel_stats(telemetry_dict):
    stats = {}

    for ch_name, data in telemetry_dict.items():
        if len(data) > 0:
            stats[ch_name] = sum(data) / len(data)
        else:
            stats[ch_name] = 0

    return stats

def filter_negative_spikes(data_list):
    return [x for x in data_list if x >= 0]