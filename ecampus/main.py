from ecampus.crawling import login, subjects

session = login('201911019', '1q2w3e4r!')
print(subjects(session, 2019, 2022))
