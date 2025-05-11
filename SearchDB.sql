SELECT 
  RSSFeeds.ID
, RSSFeeds.Name
, RSSFeeds.RSSURL
, RSSFeeds.[Desc]
, Category.CatDesc
, RSSFeeds.Subscription
, Socials.iTunes
, Socials.Instagram
, Socials.X
, Socials.YouTube
, Socials.Website
FROM RSSFeeds
LEFT JOIN Category ON Category.CatID = RSSFeeds.CatID
LEFT JOIN Socials ON Socials.ID = RSSFeeds.ID

-- WHERE Subscription = 'No'
-- WHERE CatDesc = 'News'
-- WHERE Name like '%Fox%'
-- WHERE Subscription = 'No' and CatDesc = 'News'