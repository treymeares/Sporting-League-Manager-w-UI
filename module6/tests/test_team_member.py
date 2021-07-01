from module6.fake_emailer import FakeEmailer
from module6.team_member import TeamMember
import unittest
from module6.emailer import Emailer


class TeamMemberTests(unittest.TestCase):
    def test_create(self):
        oid = 1
        name = "Fred"
        email = "fred.flintstone@gmail.com"
        tm = TeamMember(oid, name, email)
        self.assertEqual(oid, tm.oid)
        self.assertEqual(name, tm.name)
        self.assertEqual(email, tm.email)

    def test_equality_based_on_id(self):
        tm_1 = TeamMember(1, "name", "email")
        tm_2 = TeamMember(1, "other name", "other email")
        tm_3 = TeamMember(2, "name", "email")

        # team members must be equal to themselves
        self.assertTrue(tm_1 == tm_1)
        self.assertTrue(tm_2 == tm_2)
        self.assertTrue(tm_3 == tm_3)

        # same id are equal, even if other fields different
        self.assertTrue(tm_1 == tm_2)

        # different ids are not equal, even if other fields the same
        self.assertTrue(tm_1 != tm_3)

    def test_hash_based_on_id(self):
        tm_1 = TeamMember(1, "name", "email")
        tm_2 = TeamMember(1, "other name", "other email")
        tm_3 = TeamMember(3, "name", "email")

        # hash depends only on id
        self.assertTrue(hash(tm_1) == hash(tm_2))

        # objects with different id's may have different hash codes
        # note: this is not a requirement of the hash function but
        # for the case of id == 1 and id == 2 we can verify that their
        # hash codes are different in a REPL (just print(hash(1)) etc).
        self.assertTrue(hash(tm_1) != hash(tm_3))

    def test_string_output_of_team_member(self):
        tm_1 = TeamMember(1, "name", "email")
        tm_2 = TeamMember(1, "other name", "other email")
        tm_3 = TeamMember(2, "name", "email")

        self.assertEqual(str(tm_1), "name <email>")
        self.assertEqual(str(tm_2), "other name <other email>")
        self.assertNotEqual(str(tm_3), "other name <other email>")

    def test_emailer_in_team_member(self):
        tm_1 = TeamMember(1, "name", "trey.meares@me.com")
        tm_2 = TeamMember(1, "other name", "trey@lodestar-labs.com")
        fe = Emailer()
        fe.configure("treymeares@gmail.com")
        tm_1.send_email(fe, "Foo", "Bar")
        self.assertEqual(["trey.meares@me.com"], fe.recipients)
        self.assertEqual("Foo", fe.subject)
        self.assertEqual("Bar", fe.message)

        tm_2.send_email(fe, "Different", "Ugh")
        self.assertEqual(["trey@lodestar-labs.com"], fe.recipients)
        self.assertEqual("Different", fe.subject)
        self.assertEqual("Ugh", fe.message)


if __name__ == '__main__':
    unittest.main()
