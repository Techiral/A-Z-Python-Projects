import pygame
from random import randint

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1200, 700
FPS = 40
PADDING = 50
TOP_MARGIN = 100

WHITE = 255, 255, 255
BLACK = 0, 0, 0
COLOR_SCHEME = [(207, 227, 207), (84, 145, 85), (110, 171, 111), (174, 208, 175), (66, 113, 66)]

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont(None, 30)
pygame.display.set_caption("SortViz")


def generate(BAR_COUNT):
	BARS = []
	bar_width = (WIDTH - PADDING*2) / (BAR_COUNT)
	
	for count in range(BAR_COUNT):
		bar_height = randint(5, HEIGHT - TOP_MARGIN)
		bar = pygame.Rect(PADDING + count * bar_width , HEIGHT - bar_height, bar_width ,bar_height)
		BARS.append(bar)

	return BARS


def draw_rect(BARS):
	WIN.fill(WHITE, (0, TOP_MARGIN, WIN.get_width(), WIN.get_height() - TOP_MARGIN))
	
	for count, bar in enumerate(BARS):
		bar.x = PADDING + count * bar.width
		pygame.draw.rect(WIN, COLOR_SCHEME[count % (len(COLOR_SCHEME)-1)], bar)
	
	pygame.display.update()
	
	
def bubble_sort(arr, a=None, b=None):
	n = len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			draw_rect(arr)

			if arr[j].height > arr[j+1].height:
				arr[j], arr[j+1] = arr[j+1], arr[j]
			
			pygame.draw.rect(WIN, (255,0,0), arr[j])
			pygame.draw.rect(WIN, (0,0,255), arr[j+1])

			pygame.display.update()
			pygame.event.pump()
			clock.tick(FPS)
			

def selection_sort(arr, a=None, b=None):
	n = len(arr)

	for i in range(n):
		min_index = i
		for j in range(i+1, n):
			draw_rect(arr)

			if arr[min_index].height > arr[j].height:
				min_index = j

			pygame.draw.rect(WIN, (255,0,0), arr[j])
			pygame.display.update()
			pygame.event.pump()
			clock.tick(FPS)

		arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr, a=None, b=None):
	n = len(arr)

	for i in range(1,n):
		key = arr[i]
		j = i-1
		while j >= 0 and key.height < arr[j].height:
			draw_rect(arr)

			arr[j+1] = arr[j]
			j -= 1

			pygame.draw.rect(WIN, (255,0,0), arr[j])
			pygame.display.update()
			pygame.event.pump()
			clock.tick(FPS)

		arr[j+1] = key

	
def merge(arr, low, mid, high):
	p1 = low
	p2 = mid + 1
	m = mid

	while p1 <= m and p2 <= high:
		if arr[p1].height < arr[p2].height:
			p1 += 1
		else:
			temp = arr[p2]
			for i in range(p2, p1, -1):
				arr[i] = arr[i-1]
			
			arr[p1] = temp
			p1 += 1
			p2 += 1
			m += 1

		pygame.event.pump()
		draw_rect(arr)
		clock.tick(FPS)

	for i in range(low, high+1):
		color = (255, 0, 0) if i&1 else (0,0,255)
		pygame.draw.rect(WIN, color, arr[i])
		pygame.display.update()
		clock.tick(FPS)
	
			
def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def partition(arr, low, high):
	rand = randint(low, high)
	arr[rand], arr[high] = arr[high], arr[rand]

	pivot = arr[high].height
	i = low - 1

	for j in range(low, high):
		draw_rect(arr)

		if arr[j].height <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]

		pygame.draw.rect(WIN, (255,0,0), arr[j])
		pygame.draw.rect(WIN, (0,0,255), arr[rand])
		pygame.draw.rect(WIN, (0,255,0), arr[low])
		pygame.draw.rect(WIN, (0,255,0), arr[high])
		
		pygame.display.update()
		pygame.event.pump()
		clock.tick(FPS)

	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i + 1


def quick_sort(arr, l, r):
	if l < r:
		pivot = partition(arr, l, r)
		quick_sort(arr, l, pivot - 1)
		quick_sort(arr, pivot + 1, r)


def eventloop():
	running = True
	WIN.fill(WHITE)
	
	selected = -1
	BAR_COUNT = None
	sortingAlgo = ['Bubble sort','Selection sort', 'Insertion sort', 'Merge sort', 'Quick sort', 'Please select a sorting algorithm']
	functions = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort]

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1:
					selected = 0
					BAR_COUNT = 50
					BARS = generate(BAR_COUNT)
					draw_rect(BARS)
				elif event.key == pygame.K_2:
					selected = 1
					BAR_COUNT = 50
					BARS = generate(BAR_COUNT)
					draw_rect(BARS)
				elif event.key == pygame.K_3:
					selected = 2
					BAR_COUNT = 50
					BARS = generate(BAR_COUNT)
					draw_rect(BARS)
				elif event.key == pygame.K_4:
					selected = 3
					BAR_COUNT = 100
					BARS = generate(BAR_COUNT)
					draw_rect(BARS)
				elif event.key == pygame.K_5:
					selected = 4
					BAR_COUNT = 200
					BARS = generate(BAR_COUNT)
					draw_rect(BARS)
				elif event.key == pygame.K_RETURN:
					if BAR_COUNT != None:
						functions[selected](BARS, 0, len(BARS)-1)
						draw_rect(BARS)

		heading = FONT.render('Press 1-5 to select sorting algorithm | Press Enter to sort', True, BLACK)
		text = FONT.render('Selected Sorting algorithm : ' + sortingAlgo[selected], True, BLACK)
		
		textRect = text.get_rect()
		headingRect = heading.get_rect()

		headingRect.topleft = (PADDING, 10)
		textRect.topleft = (PADDING, 40)

		WIN.fill(WHITE, (0, 0, WIN.get_width(), TOP_MARGIN))
		WIN.blit(heading, headingRect)
		WIN.blit(text, textRect)

		pygame.display.update()
		clock.tick(FPS)
					
	pygame.quit()


eventloop()