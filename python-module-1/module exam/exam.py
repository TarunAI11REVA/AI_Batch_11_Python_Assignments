# ====================================================
# Data set for Q1. sanitized for better readability

'''
[{'name': 'Rahul',
  'scores': {'Math': 85, 'Science': 90, 'English': 78, 'Social': 88}},
 {'name': 'Priya',
  'scores': {'Math': 92, 'Science': 88, 'English': 95, 'Social': 90}},
 {'name': 'Amit',
  'scores': {'Math': 65, 'Science': 70, 'English': invalid, 'Social': 68}},
 {'name': 'Sneha',
  'scores': {'Math': 78, 'Science': 82, 'English': 85, 'Social': 80}},
 {'name': 'Vikram',
  'scores': {'Math': 45, 'Science': 50, 'English': 55, 'Social': 48}}]
'''

# ==============================

#==============================
# Q1.a.
#==============================

def parse_student_records(raw_data):
    parsed = []
    for student_record in raw_data:
        # split student name and scores by '|' since the format is "Name | subject1:score1, subject2:score2,..."
        if '|' in student_record:
            name_part, scores_part = student_record.split('|', 1)
        # handle case where '|' is missing (gracefully) - will make the code robust for malformed entries
        else:
            name_part = student_record.strip()
            scores_part = "" # assume no scores if '|' missing
        name = name_part.strip()
        # Normalize and split score entries
        scores_part = scores_part.replace("\n", "").strip()
        entries = [entry.strip() for entry in scores_part.split(',') if entry.strip()]
        
        # initialize subject map to hold subject-value pairs
        subject_map = {}
        for entry in entries:
            if ':' in entry:
                subj, val = entry.split(':', 1)
                subject_map[subj.strip()] = val.strip()
            else:
                # malformed entry, ignore
                continue
        
        # Error handling and validation
        
        # This part of the code ensures that we have all expected subjects and validates their values.
        # Will assign 0 for missing subjects or invalid values.
        EXAM_SUBJECTS_NAME = ['Math', 'Science', 'English', 'Social']
        scores = {}
        for subject in EXAM_SUBJECTS_NAME:
            raw_val = subject_map.get(subject)
            if raw_val is None:
                # assign 0 for missing subjects
                scores[subject] = 0
                continue
            # handle "invalid" or non-numeric values and assign 0
            try:
                if isinstance(raw_val, str) and raw_val.strip().lower() == 'invalid':
                    val = 0
                else:
                    val = int(float(raw_val))  # handle cases where value might be float string
            except Exception:
                val = 0
            # validate range 0-100; if out of range, set to 0
            if not (0 <= val <= 100):
                val = 0
            scores[subject] = val
        
        parsed.append({'name': name, 'scores': scores})
    return parsed

# ==============================
# TEST CODE FOR Q1.a.
# ==============================

# Q1.a. Testing the function with provided data
raw_student_data = [
    "Rahul|Math:85,Science:90,English:78,Social:88",
    "Priya|Math:92,Science:88,English:95,Social:90",
    "Amit|Math:65,Science:70,English:invalid,Social:68",
    "Sneha|Math:78,Science:82,English:85,Social:80",
    "Vikram|Math:45,Science:50,English:55,Social:48"
]
print(parse_student_records(raw_student_data))

#==============================================================================
# Q1.b. Step by step code for parse_student_records function for Amit's record
#==============================================================================

def parse_student_records(raw_data):
    parsed = []

    for student_record in raw_data:

        # STEP 1: Split the record into name part and scores part
        # Example: "Amit|Math:65,Science:70,English:invalid,Social:68"
        # becomes:
        # name_part = "Amit"
        # scores_part = "Math:65,Science:70,English:invalid,Social:68"
        if '|' in student_record:
            name_part, scores_part = student_record.split('|', 1)
        else:
            name_part = student_record.strip()
            scores_part = ""

        # STEP 2: Clean & strip whitespace from the student's name
        name = name_part.strip()

        # STEP 3: Normalize scores part (remove stray newlines)
        scores_part = scores_part.replace("\n", "").strip()

        # STEP 4: Split the scores part into individual entries
        # Example: "Math:65,Science:70,English:invalid,Social:68"
        # becomes:
        # ["Math:65", "Science:70", "English:invalid", "Social:68"]
        entries = [entry.strip() for entry in scores_part.split(',') if entry.strip()]

        # STEP 5: Split each entry into subject and raw value
        subj_map = {}
        for entry in entries:
            if ':' in entry:
                subj, val = entry.split(':', 1)
                subj_map[subj.strip()] = val.strip()
            # malformed entries are ignored

        # STEP 6–9: Validate, convert, and clean each subject score
        EXAM_SUBJECTS_NAME = ['Math', 'Science', 'English', 'Social']
        scores = {}
        for subj in EXAM_SUBJECTS_NAME:
            raw_val = subj_map.get(subj)

            # STEP 6: If subject missing → assign 0
            if raw_val is None:
                scores[subj] = 0
                continue

            # STEP 7: Detect "invalid" and convert it to 0
            if isinstance(raw_val, str) and raw_val.lower() == 'invalid':
                val = 0
            else:
                # STEP 8: Try converting to a number
                try:
                    val = int(float(raw_val))
                except Exception:
                    val = 0

            # STEP 9: Validate range (0–100). If invalid, set to 0
            if not (0 <= val <= 100):
                val = 0

            scores[subj] = val

        # STEP 10: Build final parsed dictionary for the student
        parsed.append({
            'name': name,
            'scores': scores
        })

    return parsed


# ==============================
# Q2.a.
# ==============================

def calculate_student_grades(student_records):

    # this small helper funcion picks the grade based on the avg score
    def get_grade(avg):
        if 90 <= avg <= 100:
            return "A+"
        elif 80 <= avg <= 89:
            return "A"
        elif 70 <= avg <= 79:
            return "B+"
        elif 60 <= avg <= 69:
            return "B"
        elif 50 <= avg <= 59:
            return "C"
        else:
            return "F"

    # go through each student one by one
    for student in student_records:
        
        # get all the marks the student has in the dictionary
        scores = student['scores']

        # calculate the avarage (simple mean of 4 subjects)
        avg = sum(scores.values()) / len(scores)

        # get the grade from the helper functiona
        grade = get_grade(avg)

        # decide if the student passed or failed
        # pass means average is 50 or more
        status = "Pass" if avg >= 50 else "Fail"

        # add the new fields (average, grade, and status) back into the student's record
        student['average'] = round(avg, 2)
        student['grade'] = grade
        student['status'] = status

    # return the updated list with all the newly added fields.
    return student_records

# Q2.a. Testing the function with parsed student data
parsed_data = parse_student_records(raw_student_data)
print(calculate_student_grades(parsed_data))


# =====================================================
# Q2.b. Uses pandas and matplotlib to generate a table.
# Output of Q2.a. function is used as input.
# ======================================================

import pandas as pd
import matplotlib.pyplot as plt

# function to generate and display the table
# it takes the graded student records as input from Q2.a. function and then generates a table
def generate_student_table(graded_records):
    rows = []

    for student in graded_records:
        row = {
            "Student": student["name"],
            "Math": student["scores"]["Math"],
            "Science": student["scores"]["Science"],
            "English": student["scores"]["English"],
            "Social": student["scores"]["Social"],
            "Average": student["average"],
            "Grade": student["grade"],
            "Status": student["status"]
        }
        rows.append(row)

    # Create DataFrame
    df = pd.DataFrame(rows)
    print(df)

    # matplotlib visual table
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.axis("off")

    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        loc="center"
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    plt.tight_layout()
    plt.show()
    

# =============================
# TEST CODE FOR Q2.b.
# =============================
    
# Testing the function with graded student data    

# calculate grades
graded_output = calculate_student_grades(parsed_data)

# generate table from it
generate_student_table(graded_output)

# ==============================
# Q3.a.
# ==============================

import numpy as np

def class_statistics(student_records):
    # Extract all averages into a NumPy array
    averages = np.array([student['average'] for student in student_records])

    # Calculate required statistics
    class_mean = np.mean(averages)
    class_median = np.median(averages)
    class_std = np.std(averages)

    # Highest and lowest scorer indexes
    highest_index = np.argmax(averages)
    lowest_index = np.argmin(averages)

    # store highest and lowest scorer details in dictionaries
    highest_scorer = {
        "name": student_records[highest_index]["name"],
        "average": float(round(averages[highest_index], 2))
    }

    lowest_scorer = {
        "name": student_records[lowest_index]["name"],
        "average": float(round(averages[lowest_index], 2))
    }

    # Count how many scored above class average
    above_avg_count = np.sum(averages > class_mean)

    # Pass percentage
    pass_count = np.sum(averages >= 50)
    pass_percentage = (pass_count / len(student_records)) * 100

    # Return everything structured
    return {
        "class_mean": float(round(class_mean, 2)),
        "class_median": float(round(class_median, 2)),
        "class_std_dev": float(round(class_std, 2)),
        "highest_scorer": highest_scorer,
        "lowest_scorer": lowest_scorer,
        "above_average_count": int(above_avg_count),
        "pass_percentage": float(round(pass_percentage, 2))
    }
    
# =============================
# TEST CODE FOR Q3.a.
# =============================

# Testing the function with graded student data
stats = class_statistics(graded_output)
print(stats)

# ==============================
# Q3.b.
# ==============================

# Array used for calculations: Its the average scores of the 5 students obtained from Q2.a.
# A = [85.25, 91.25, 50.75, 81.25, 49.50]
#
# 1. MEAN CALCULATION
# Sum = 85.25 + 91.25 + 50.75 + 81.25 + 49.50 = 358.00
# Mean = 358.00 / 5 = 71.6
#
# 2. MEDIAN CALCULATION
# Sorted array = [49.50, 50.75, 81.25, 85.25, 91.25]
# Middle value (3rd element) = 81.25
# Median = 81.25
#
# 3. STANDARD DEVIATION CALCULATION
# Deviations and Squares: Devaiations from Mean (71.6) and their squares
# 85.25 - 71.6 = 13.65
# squaring, 13.65^2 = 186.3225
# 91.25 - 71.6 = 19.65 
# squaring, 19.65^2 = 386.1225
# 50.75 - 71.6 = -20.85 
# squaring, (-20.85)^2 = 434.7225
# 81.25 - 71.6 = 9.65 
# squaring, 9.65^2 = 93.1225
# 49.50 - 71.6 = -22.10 
# squaring, (-22.10)^2 = 488.4100
# Sum of all squares = 1588.70
# Variance = 1588.70 / 5 = 317.74
# Std Dev = sqrt(317.74) = 17.83
#
# 4. PASS PERCENTAGE
# Pass if average >= 50 (this is from Q2.a. criteria, or from the main criteria of the problem)
# Passed: 85.25, 91.25, 50.75, 81.25 (4 students)
# Failed: 49.50 (1 student)
# Pass % = (4 / 5) * 100 = 80%

# ==============================
# Q4.a.
# ==============================

def subject_wise_performance(student_records):
    
    # keep a dictionary for storing all marks subject wise
    subjects = {
        "Math": [],
        "Science": [],
        "English": [],
        "Social": []
    }

    # store (name, score) pairs to find highest and lowest later
    subject_with_names = {
        "Math": [],
        "Science": [],
        "English": [],
        "Social": []
    }

    # go through every single student
    for student in student_records:
        name = student["name"]
        scores = student["scores"]

        # add their scores into the correct subject bucket
        for subject, value in scores.items():
            subjects[subject].append(value)
            subject_with_names[subject].append((name, value))

    # final place to store all results
    subject_wise_statistics = {}

    # now we calc stats for each subject one by one
    for subject in subjects:

        scores = subjects[subject]
        name_score_pairs = subject_with_names[subject]

        # calculate the avarage marks for this subject
        avg_score = sum(scores) / len(scores)

        # find highest scorer, pick the (name,score) with max score
        highest = max(name_score_pairs, key=lambda x: x[1])
        # same thing but for lowest
        lowest = min(name_score_pairs, key=lambda x: x[1])

        # count students above 75 score
        above_75 = sum(1 for s in scores if s > 75)

        # save everything in statistics dictionary
        subject_wise_statistics[subject] = {
            "average": round(avg_score, 2),
            "highest_scorer": highest[0],
            "highest_score": highest[1],
            "lowest_scorer": lowest[0],
            "lowest_score": lowest[1],
            "above_75_count": above_75
        }

    # identify which subject has the best (highest) class avg
    best_subject = max(subject_wise_statistics.items(), key=lambda x: x[1]["average"])[0]

    # return both: subject stats and the best one
    return {
        "subject_stats": subject_wise_statistics,
        "best_subject": best_subject
    }

# =============================
# Q.4.b
# =============================






# ==============================
# Q5.a.
# ==============================

def generate_student_report(student_name, student_records):
    """
    student_name: string
    student_records: list of dicts like:
        {
            'name': 'Rahul',
            'scores': {'Math': 85, 'Science': 90, 'English': 78, 'Social': 88}
        }
    """
    try:
        # Find student (case-insensitive)
        student = None
        for record in student_records:
            if record['name'].lower() == student_name.lower():
                student = record
                break

        if student is None:
            raise ValueError(f"Student '{student_name}' not found")

        scores = student['scores']
        score_values = list(scores.values())
        average = sum(score_values) / len(score_values)

        # Determine grade
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        status = "Pass" if average >= 60 else "Fail"

        # Build formatted report
        report_lines = [
            f"Report for {student['name']}",
            "---------------------------",
            "Scores:"
        ]

        for subject, score in scores.items():
            report_lines.append(f"  {subject}: {score}")

        report_lines.extend([
            f"Average Score: {average:.2f}",
            f"Grade: {grade}",
            f"Status: {status}"
        ])

        return "\n".join(report_lines)

    except ValueError as e:
        return f"Error: {e}"

    finally:
        print("Report generation attempted")
        
# =============================
# Q5.b.
# =============================

rahul_record = generate_student_report("Rahul", parse_student_records(raw_student_data))
print(rahul_record)
'''
Report for Rahul
---------------------------
Scores:
  Math: 85
  Science: 90
  English: 78
  Social: 88
Average Score: 85.25
Grade: B
Status: Pass
Report generation attempted
'''

rahul_record = generate_student_report("priya", parse_student_records(raw_student_data))
print(rahul_record)

'''
Report for Priya
---------------------------
Scores:
  Math: 92
  Science: 88
  English: 95
  Social: 90
Average Score: 91.25
Grade: A
Status: Pass
Report generation attempted
'''

rahul_record = generate_student_report("invalid name", parse_student_records(raw_student_data))
print(rahul_record)
'''
Error: Student 'invalid name' not found
Report generation attempted
'''

rahul_record = generate_student_report("", parse_student_records(raw_student_data))
print(rahul_record)

'''
Error: Student '' not found
Report generation attempted
'''

# ==============================
# Q6.a.
# ==============================

def parse_and_add_student(student_str, student_records):
    """
    Parse a string like:
    'Kavya|Math:88,Science:92,English:85,Social:90'
    Validate it, convert it into the student dict format, and append it.
    """

    try:
        # Split name and score
        if "|" not in student_str:
            raise ValueError("Input must contain '|' separating name and scores")
        
        name, scores_part = student_str.split("|", 1)
        name = name.strip()

        if not name:
            raise ValueError("Student name cannot be empty")

        # Parse subjects and scores
        score_pairs = scores_part.split(",")
        scores = {}

        for pair in score_pairs:
            if ":" not in pair:
                raise ValueError(f"Invalid score format in '{pair}'")

            subject, value = pair.split(":", 1)
            subject = subject.strip()
            value = value.strip()

            if not value.isdigit():
                raise ValueError(f"Score for {subject} must be a number")

            scores[subject] = int(value)

        # Construct student dict
        new_student = {
            "name": name,
            "scores": scores
        }

        # Append to the main records
        student_records.append(new_student)
        return student_records

    except ValueError as e:
        return f"Error: {e}"
    
# Recompute grades after adding new student
parsed_student_records = parse_student_records(raw_student_data)
updated_student_records = parse_and_add_student('Kavya|Math:88,Science:92,English:85,Social:90', parsed_student_records)
print(updated_student_records)
updated_student_grades = calculate_student_grades(updated_student_records)
print(updated_student_grades)

# Recompute class statistics after adding new student
updated_class_stats = class_statistics(parsed_student_records)    
print(updated_class_stats)
    
# ==============================
# Q6.b.
# ==============================

# class stats before Kavya addition
parsed_student_records = parse_student_records(raw_student_data)
student_grades = calculate_student_grades(parsed_student_records)
class_stats = class_statistics(student_grades)

# class statistics after adding new student
updated_class_stats = class_statistics(parsed_student_records)    
print(updated_class_stats)

# before Kavya addition
generate_student_table(parsed_student_records)

# after Kavya addition
generate_student_table(updated_student_grades)

# ==============================
# Q6.c.
# ==============================

import pandas as pd
import matplotlib.pyplot as plt

# helper function to compute class statistics
def compute_stats(students):
    df = pd.DataFrame([{
        'name': s['name'],
        'avg': sum(s['scores'].values()) / len(s['scores'])
    } for s in students])

    class_mean = df['avg'].mean()
    class_median = df['avg'].median()
    pass_percent = (df['avg'] >= 60).mean() * 100
    above_avg = (df['avg'] > class_mean).sum()

    return class_mean, class_median, pass_percent, above_avg


students_before = parse_student_records(raw_student_data)

# Add Kavya
students_after = parse_and_add_student('Kavya|Math:88,Science:92,English:85,Social:90', students_before)

# Compute statistics
before_stats = compute_stats(students_before)
after_stats = compute_stats(students_after)

comparison_df = pd.DataFrame({
    "Metric": ["Class Mean", "Class Median", "Pass %", "Students Above Avg"],
    "Before": before_stats,
    "After": after_stats
})

print("\nComparison Table:")
print(comparison_df)

# Plot graph: Before vs After
plt.figure(figsize=(10, 5))
plt.plot(comparison_df["Metric"], comparison_df["Before"], marker='o', label="Before")
plt.plot(comparison_df["Metric"], comparison_df["After"], marker='o', label="After")

plt.xlabel("Metric")
plt.ylabel("Value")
plt.title("Class Statistics Before vs After Adding Kavya")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

print(plt.show())

# ==============================
# Q7.a.
# ==============================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
red = pd.read_csv('module exam/winequality-red.csv', sep=';')
white = pd.read_csv('module exam/winequality-white.csv', sep=';')

# Add labels
red['wine_type'] = 'red'
white['wine_type'] = 'white'

# Combine datasets
df = pd.concat([red, white], ignore_index=True)

# Dataset dimensions
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")

# Missing values
print(df.isna().sum())

# Statistical summary for key features
stats = df[['alcohol', 'pH', 'quality']].describe()
print(stats)

# Quality distribution
quality_dist = df['quality'].value_counts().sort_index()
print(quality_dist)

# summary table
summary = pd.DataFrame({
    "Total Samples": [df.shape[0]],
    "Feature Count": [df.shape[1]],
    "Mean Alcohol": [df['alcohol'].mean()],
    "Mean pH": [df['pH'].mean()],
    "Mean Quality": [df['quality'].mean()],
    "Quality Range": [f"{df['quality'].min()} - {df['quality'].max()}"],
    "Most Common Quality": [df['quality'].mode()[0]]
})

print(summary)


# ==============================
# Q8.a.
# ==============================

# the dataframe "df" is already loaded and combined
# with red and white wines from Q7.a.
# columns: alcohol, pH, quality, wine_type

# Create a 2×2 grid of subplots to display all four charts
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# HISTOGRAM OF ALCOHOL CONTENT (TOP-LEFT)
# This histogram shows how alcohol levels are distributed across all wines.
# We also draw a red dashed line to indicate the mean alcohol value,
# helping us quickly see whether most wines fall above or below the average.
ax = axes[0, 0]
ax.hist(df['alcohol'], bins=30, edgecolor='black', alpha=0.7)
ax.axvline(df['alcohol'].mean(), color='red', linestyle='--', linewidth=2,
           label=f"Mean: {df['alcohol'].mean():.2f}")
ax.set_title("Alcohol Content Distribution")
ax.set_xlabel("Alcohol (%)")
ax.set_ylabel("Frequency")
ax.legend()

# BAR CHART OF QUALITY RATING FREQUENCIES (TOP-RIGHT)
# This bar chart shows how many wines received each quality score.
# It helps us understand whether certain quality ratings (like 5 or 6)
# dominate the dataset.
ax = axes[0, 1]
quality_counts = df['quality'].value_counts().sort_index()
ax.bar(quality_counts.index, quality_counts.values, color='skyblue', edgecolor='black')
ax.set_title("Wine Quality Ratings")
ax.set_xlabel("Quality Score")
ax.set_ylabel("Count")

# BOX PLOT OF pH LEVELS BY WINE TYPE (BOTTOM-LEFT)
# This box plot compares acidity levels (pH) between red and white wines.
# Each wine type gets one box, showing the distribution, median, and outliers.
# It helps identify whether red and white wines differ significantly in pH.
ax = axes[1, 0]
sns.boxplot(data=df, x='wine_type', y='pH', ax=ax, palette='Set2')
ax.set_title("pH Levels by Wine Type")
ax.set_xlabel("Wine Type")
ax.set_ylabel("pH Level")

# SCATTER PLOT: ALCOHOL VS QUALITY (BOTTOM-RIGHT)
# This scatter plot explores whether alcohol content affects wine quality.
# Each point is one wine sample.
# Points are colored by wine type to compare red vs. white patterns.
ax = axes[1, 1]
sns.scatterplot(
    data=df,
    x='alcohol',
    y='quality',
    hue='wine_type',
    palette='Set1',
    alpha=0.7,
    ax=ax
)
ax.set_title("Alcohol vs. Quality by Wine Type")
ax.set_xlabel("Alcohol (%)")
ax.set_ylabel("Quality Rating")
ax.legend(title="Wine Type")

# adjust spacing so titles and labels don’t overlap
plt.tight_layout()

# display the complete 2×2 grid of plots
print(plt.show())

# ==============================
# Q9.a.
# ==============================

# Combine both datasets
df = pd.concat([red, white], ignore_index=True)

# Select key features that may influence wine quality
# These features are known to affect taste, aroma, and stability
features = [
    "alcohol",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "pH",
    "sulphates",
    "quality"
]

data = df[features]

# correlation matrix
# This tells us how strongly each chemical property moves
# together with wine quality (+ = positive influence, - = negative)
corr_matrix = data.corr()

print(corr_matrix)

# Create a heatmap to visualize correlation strength
# Colors show the strength of the relationship:
# - Dark red = strong positive correlation
# - Dark blue = strong negative correlation
# - Light colors = weak or no correlation
plt.figure(figsize=(10, 6))
sns.heatmap(
    corr_matrix,
    annot=True,          # Show correlation values inside the cells
    cmap="coolwarm",     # Color scale: blue -> red
    fmt=".2f",           # Show values with 2 decimal places
    square=True,
    linewidths=0.5
)

plt.title("Correlation Heatmap of Key Wine Chemical Properties", fontsize=14)
plt.tight_layout()
print(plt.show())

# Identify top positive & negative correlations with wine quality
quality_corr = corr_matrix["quality"].sort_values(ascending=False)

print(quality_corr)

# Most positively correlated feature (besides quality itself)
top_positive = quality_corr.iloc[1]    # skip first because it's 1.0 (quality with quality)
top_positive_feature = quality_corr.index[1]

# Most negatively correlated feature
top_negative = quality_corr.iloc[-1]
top_negative_feature = quality_corr.index[-1]

# ======================================
# Q10.a.
# ======================================

# Add a new column so we know which wine type each row represents
red["wine_type"] = "Red"
white["wine_type"] = "White"

# Combine them into one dataset for easy comparison
df = pd.concat([red, white], ignore_index=True)

# Select the three features we want to compare:
#    - alcohol
#    - residual sugar
#    - pH
#
# violin plots for each to compare distribution between red and white wines.
features = ["alcohol", "residual sugar", "pH"]

# Create subplots side by side
plt.figure(figsize=(18, 6))

for i, feature in enumerate(features):
    plt.subplot(1, 3, i + 1)

    # Violin plot shows data distribution and density
    sns.violinplot(
        data=df,
        x="wine_type",
        y=feature,
        inner="quartile",   # shows median and quartiles inside the violin
        linewidth=1.2,
        color="gold"
    )

    plt.title(f"Violin Plot of {feature}", fontsize=16)
    plt.xlabel("Wine Type")
    plt.ylabel(feature)

plt.tight_layout()
print(plt.show())

# Calculate mean values for red vs white wines for each feature.
#    This helps measure actual numeric differences beyond visuals.
comparison = (
    df.groupby("wine_type")[features]
    .mean()
    .T  # transpose so features appear as rows
)

# Add a column showing how much white differs from red
comparison["Difference (White - Red)"] = (
    comparison["White"] - comparison["Red"]
)

# Print the comparison table
print("\nStatistical Comparison Between Red and White Wines:\n")
print(comparison)


