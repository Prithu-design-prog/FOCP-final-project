import sys

def cat_visit_log(filename):
    # Analyzes a log file containing cat visit data.

    try:
        # Attempt to open and read the specified file
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        # Handle the case when the file is not found
        print(f"Cannot open file: {filename}")
        return
    except PermissionError:
        # Handle the case when there are insufficient permissions to open the file
        print(f"Insufficient permissions to open file: {filename}")
        return

    # Initialize variables for cat visit statistics
    cat_visits = 0
    intruder_encounters = 0
    total_cat_time = 0
    cat_visit_durations = []

    for line in lines:
        # Exit the loop when "END" is encountered in the log file
        if "END" in line:
            break

        try:
            # Parse data from the log file line
            cat, entry_time, exit_time = line.strip().split(",")
            entry_minutes = int(entry_time)
            exit_minutes = int(exit_time)
        except ValueError:
            # Handle the case when the data format is invalid
            print(f"Invalid data format in line: {line}")
            continue

        if cat == "OURS":
            # Update statistics for our cat's visits
            cat_visits += 1
            visit_duration = exit_minutes - entry_minutes
            cat_visit_durations.append(visit_duration)
            total_cat_time += visit_duration
        else:
            # Update statistics for encounters with other cats
            intruder_encounters += 1

    # Calculate additional statistics based on collected data
    average_visit_length = sum(cat_visit_durations) / len(cat_visit_durations) if cat_visit_durations else 0
    average_visit_length = round(average_visit_length, 2)  # Round to 2 decimal places

    longest_visit = max(cat_visit_durations) if cat_visit_durations else 0
    shortest_visit = min(cat_visit_durations) if cat_visit_durations else 0

    hours = total_cat_time // 60
    minutes = round(total_cat_time % 60, 2)  # Round to 2 decimal places

    # Display the analysis results
    print("Log File Analysis")
    print("==================")
    print(f"Cat Visits: {cat_visits}")
    print(f"Other Cats: {intruder_encounters}")
    print(f"Total Time in House: {hours} Hours, {minutes} Minutes")
    print(f"Average Visit Length: {average_visit_length} Minutes")
    print(f"Longest Visit: {longest_visit} Minutes")
    print(f"Shortest Visit: {shortest_visit} Minutes")

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Missing command line argument! Please provide the log file.")
    else:
        # Extract the filename from the command-line arguments and perform the analysis
        filename = sys.argv[1]
        cat_visit_log(filename)
