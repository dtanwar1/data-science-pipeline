import utils.mongo_db_client as mdc

#script to get collected data count
t_col = mdc.getCollection("kek_db", "twitter")
r_col = mdc.getCollection("kek_db", "reddit")
rp_col = mdc.getCollection("kek_db", "reddit_politics")
y_col = mdc.getCollection("kek_db", "youtube")
rpc = rp_col.count_documents({})
rc = r_col.count_documents({})
tc = t_col.count_documents({})
yc = y_col.count_documents({})
mdc.insert({
    "param":"totalDataC",
    "value":rpc+tc+rc+yc
    },
    "data_aggregates",False)
