import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            default=10,
            help='Number of users to create'
        )
        parser.add_argument(
            '--listings',
            type=int,
            default=20,
            help='Number of listings to create'
        )
        parser.add_argument(
            '--bookings',
            type=int,
            default=50,
            help='Number of bookings to create'
        )
        parser.add_argument(
            '--reviews',
            type=int,
            default=30,
            help='Number of reviews to create'
        )

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')
        
        # Create users
        num_users = options['users']
        users = []
        for i in range(num_users):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123',
                first_name=fake.first_name(),
                last_name=fake.last_name()
            )
            users.append(user)
            self.stdout.write(f'Created user: {user.username}')
        
        # Create listings
        num_listings = options['listings']
        property_types = [choice[0] for choice in Listing.PROPERTY_TYPES]
        cities = ['New York', 'Los Angeles', 'Chicago', 'Miami', 'San Francisco', 'Seattle', 'Austin', 'Boston']
        countries = ['USA', 'USA', 'USA', 'USA', 'USA', 'Canada', 'Mexico', 'UK']
        
        listings = []
        for i in range(num_listings):
            city_idx = i % len(cities)
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                address=fake.address(),
                city=cities[city_idx],
                country=countries[city_idx % len(countries)],
                property_type=random.choice(property_types),
                price_per_night=random.randint(50, 500),
                max_guests=random.randint(1, 10),
                num_bedrooms=random.randint(1, 5),
                num_beds=random.randint(1, 6),
                num_bathrooms=random.randint(1, 3),
                amenities=', '.join(fake.words(nb=5)),
                is_available=random.choice([True, False]),
                owner=random.choice(users)
            )
            listings.append(listing)
            self.stdout.write(f'Created listing: {listing.title}')
        
        # Create bookings
        num_bookings = options['bookings']
        status_choices = [choice[0] for choice in Booking.STATUS_CHOICES]
        
        for i in range(num_bookings):
            listing = random.choice(listings)
            guest = random.choice(users)
            
            # Ensure guest is not the owner
            while guest == listing.owner:
                guest = random.choice(users)
            
            check_in = fake.date_between(start_date='-30d', end_date='+30d')
            check_out = check_in + timedelta(days=random.randint(1, 14))
            
            booking = Booking.objects.create(
                listing=listing,
                guest=guest,
                check_in_date=check_in,
                check_out_date=check_out,
                num_guests=random.randint(1, listing.max_guests),
                total_price=listing.price_per_night * (check_out - check_in).days,
                status=random.choice(status_choices),
                special_requests=fake.sentence() if random.choice([True, False]) else ''
            )
            self.stdout.write(f'Created booking #{booking.id}')
        
        # Create reviews
        num_reviews = options['reviews']
        
        for i in range(num_reviews):
            listing = random.choice(listings)
            guest = random.choice(users)
            
            # Ensure guest is not the owner
            while guest == listing.owner:
                guest = random.choice(users)
            
            # Check if this guest has already reviewed this listing
            if Review.objects.filter(listing=listing, guest=guest).exists():
                continue
            
            review = Review.objects.create(
                listing=listing,
                guest=guest,
                rating=random.randint(1, 5),
                comment=fake.paragraph(nb_sentences=3)
            )
            self.stdout.write(f'Created review by {guest.username} for {listing.title}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully seeded database with {num_users} users, '
                f'{num_listings} listings, {num_bookings} bookings, '
                f'and {num_reviews} reviews'
            )
        )