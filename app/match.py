import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
members = pd.read_csv("data/members.csv")

# Encode skills as feature vectors (simplified)
skills_set = list(set(";".join(members["skills"]).split(";")))
for skill in skills_set:
    members[skill] = members["skills"].apply(lambda x: 1 if skill in x else 0)

# Prepare feature set
features = ["experience", "performance"] + skills_set
X = members[features]

# Standardize and apply clustering
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=3, random_state=42)
members["cluster"] = kmeans.fit_predict(X_scaled)

def match_talent(project_skills):
    """Finds the best match for a given project based on required skills."""
    project_vector = [1 if skill in project_skills else 0 for skill in skills_set]
    scores = members[skills_set].dot(project_vector)  # Skill matching score
    top_matches = members.loc[scores.nlargest(3).index, ["name", "skills", "performance"]]
    return top_matches.to_dict(orient="records")
