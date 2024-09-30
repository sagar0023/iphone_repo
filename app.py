import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
import iphone_data
# Sample DataFrame with iPhone ratings and their frequencies
data = {
    'Rating': [1, 2, 3, 4, 5],
    'Frequency': [50, 100, 150, 400, 800]  # Frequencies of each rating
}

df = pd.DataFrame(data)


def get_opinion(frequency,rating):
    if frequency >= 100:
        return f"""This iphone has been rated {rating} by more than {frequency} users.
        Therefore you can consider this iphone."""
    elif frequency >= 50:
        return f"""This iphone is not so quite popular among the users.
                    as it has been rated {rating} by only {frequency} users.
                    You could look for other iphones. """
    else:
        return "There's not enough data to state any opinion."


st.set_page_config(layout='wide',page_title='Iphone Buying Guide')
original_df = pd.read_csv("iphone.csv")
original_df.dropna(inplace=True)
st.title("Simplifying your :blue[Iphone]:apple: Buying Experience")

logo_url = 'https://thumbs.dreamstime.com/b/apple-logo-19106337.jpg'
st.logo(logo_url)
st.sidebar.title('Select your Model')
asin_list = original_df.variantAsin.unique()

option = st.sidebar.selectbox('Select Iphone',['iPhone15','iPhone14','iPhone13'])
if option == 'iPhone15':
    
    selected = st.sidebar.selectbox('Select iPhone Model',[i['model'] for i in iphone_data.iPhones['iPhone15']])
    st.header(selected)
elif option == 'iPhone14':
    selected = st.sidebar.selectbox('Select iPhone Model',[i['model'] for i in iphone_data.iPhones['iPhone14']])
    st.header(selected)
else:
    selected = st.sidebar.selectbox('Select iPhone Model',[i['model'] for i in iphone_data.iPhones['iPhone13']])
    st.header(selected)

iphone_df = original_df[original_df.variantAsin.isin(iphone_data.find_product_id(option,selected))]
with st.container():
    iphone_details = iphone_data.find_iphone_details(option,selected)
    st.subheader(f"Overview")
    for key, value in iphone_details.items():
        if key == 'productId':
            continue
        st.write(f"{key}: {value}")
st.header("Buyer's initial impressions")
initial_views = iphone_df.reviewTitle.unique()
columns = st.columns(5 if initial_views.size > 5 else initial_views.size)
for index,col in enumerate(columns):
    with col:
        st.write(initial_views[index])


chart_data = iphone_df['ratingScore'].value_counts().reset_index()

col_1, col_2 = st.columns(2)

with col_1:
    st.subheader("Rating Graph")
    
    fig, ax = plt.subplots()
    ax.bar(chart_data['ratingScore'], chart_data['count'], color='red')
    ax.set_xlabel("Rating Score")
    ax.set_ylabel("Frequency")
    ax.set_title("Distribution of Ratings")

    st.pyplot(fig)

with col_2:
    temp_df = pd.DataFrame({
        'Category': ['Total iPhones in Market', f'{option} in Market'],
        'Count': [original_df.shape[0], iphone_df.shape[0]]
    })

    # Prepare data for pie chart
    labels = temp_df['Category']
    sizes = temp_df['Count']

    # Create a pie chart
    st.subheader(f'Presence of {option} in market')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax1.axis('equal')  # Equal aspect ratio ensures that the pie chart is drawn as a circle.

    # Display the pie chart in Streamlit
    st.pyplot(fig1)

chart_data.reset_index(inplace=True)
highest_freq_row = chart_data.loc[chart_data['count'].idxmax()]
highest_rating = highest_freq_row['ratingScore']
highest_frequency = highest_freq_row['count']

st.subheader('Our Opinion')
st.write(get_opinion(highest_frequency,highest_rating))





pos_review = iphone_df[iphone_df['ratingScore'].isin([4,5])].head()
neg_review = iphone_df[iphone_df['ratingScore'].isin([1,2])].head()
critic_review = iphone_df[iphone_df['ratingScore'].isin([3])].head()
st.subheader("Popular Positive Reviews")
container1 = st.container(border=True)
st.subheader('Popular Negative Reviews')
container2 = st.container(border=True)
st.subheader('Critic Reviews')
container3 = st.container(border=True)

if pos_review.shape[0]:
    for index, row in pos_review.iterrows():
        container1.markdown(f"{row['reviewDescription']} [Link]({row['reviewUrl']})")
else:
    container1.write("No positive reviews available.")

# Handle negative reviews
if neg_review.shape[0]:
    for index, row in neg_review.iterrows():
        container2.markdown(f"{row['reviewDescription']} [Link]({row['reviewUrl']})")
else:
    container2.write("No negative reviews available.")

# Handle critic reviews
if critic_review.shape[0]:
    for index, row in critic_review.iterrows():
        container3.markdown(f"{row['reviewDescription']} [Link]({row['reviewUrl']})")
else:
    container3.write("No critic reviews available.")
 
st.divider()
st.write('These are real reviews given by a verified buyer.')
st.write('Source : amazon database')
st.markdown('contact - sagarsharma23112@gmail.com')
















