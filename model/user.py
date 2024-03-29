from marshmallow import Schema, fields


class User(object):
    def __init__(self, id, email, emailVerified, profilePictureUrl, provider, username, matchesPlayed, matchesWon, eloRank, country, signupDate):
        self.email = email
        self.emailVerified = emailVerified
        self.profilePictureUrl = profilePictureUrl
        self.provider = provider
        self.id = id
        self.username = username
        self.matchesPlayed = matchesPlayed
        self.matchesWon = matchesWon
        self.eloRank = eloRank
        self.country = country
        self.signupDate = signupDate


class UserSchema(Schema):
    email = fields.String()
    emailVerified = fields.Boolean()
    profilePictureUrl = fields.String()
    provider = fields.String()
    id = fields.String()
    username = fields.String()
    matchesPlayed = fields.Integer()
    matchesWon = fields.Integer()
    eloRank = fields.Float()
    country = fields.String()
    signupDate = fields.String()