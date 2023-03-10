import { useState } from 'react'

import { Container } from '@/components/Container'
import { SectionHeading } from '@/components/SectionHeading'

const tableOfContents = {
  'Getting started': {
    'Getting started': 1,
    'Intro to Figma': 15,
    'Setting up your first artboard': 20,
  },
  Fundamentals: {
    'Strokes and fills': 21,
    'End points': 22,
    'Bezier curves': 26,
    'Designing on a grid': 31,
    'Vector shapes': 45,
  },
  'Boolean operations': {
    'Combining shapes': 50,
    'Subtracting shapes': 57,
    'Intersecting shapes': 66,
    Flattening: 78,
  },
  'Optimizing for production': {
    'Preparing for SVG': 82,
    'Configuring your export settings': 88,
    'Minifying and removing metadata': 95,
  },
}

export function TableOfContents() {
  let [isExpanded, setIsExpanded] = useState(false)

  return (
    <section
      id="table-of-contents"
      aria-labelledby="table-of-contents-title"
      className="scroll-mt-14 py-16 sm:scroll-mt-32 sm:py-20 lg:py-32"
    >
      <Container>
        <SectionHeading number="1" id="table-of-contents-title">
          Table of contents
        </SectionHeading>
        <p className="mt-8 font-display text-4xl font-bold tracking-tight text-slate-900">
          Get a look at all of the content covered in the book. Everything you
          need to know is inside.
        </p>
        <p className="mt-4 text-lg tracking-tight text-slate-700">
          “Everything Starts as a Square” is comprised of 240 tightly edited,
          highly visual pages designed to teach you everything you need to know
          about icon design with no unnecessary filler.
        </p>
        <ol className="mt-16 space-y-10 sm:space-y-16">
          {Object.entries(tableOfContents)
            .slice(0, isExpanded ? undefined : 2)
            .map(([title, pages]) => (
              <li key={title}>
                <h3 className="font-display text-3xl font-bold tracking-tight text-slate-900">
                  {title}
                </h3>
                <ol className="mt-8 divide-y divide-slate-300/30 rounded-2xl bg-slate-50 py-3 px-6 text-base tracking-tight sm:py-7 sm:px-8">
                  {Object.entries(pages).map(([title, pageNumber]) => (
                    <li key={title} className="flex justify-between py-3">
                      <span className="font-medium text-slate-900">
                        {title}
                      </span>
                      <span className="font-mono text-slate-400">
                        <span className="sr-only">on page {pageNumber}</span>
                        <span aria-hidden="true">{pageNumber}</span>
                      </span>
                    </li>
                  ))}
                </ol>
              </li>
            ))}
        </ol>
        {!isExpanded && (
          <div className="mt-10 flex justify-center">
            <button
              type="button"
              className="flex items-center text-base font-medium tracking-tight text-slate-900 hover:text-slate-700"
              onClick={() => setIsExpanded(true)}
            >
              See more
              <svg aria-hidden="true" className="ml-2 h-6 w-6">
                <path
                  d="m17 14-5 5-5-5M12 18.5V5"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </button>
          </div>
        )}
      </Container>
    </section>
  )
}
